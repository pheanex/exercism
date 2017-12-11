class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    def process(stack):
        if not any(stack):
            return []
        if not len(stack) > 0:
            raise StackUnderflowError
        if len(stack) == 1 and stack[-1].isdigit():
            return int(stack[-1])
        if stack[-1].lower() in alias:
            return process(stack[:-1] + alias[stack[-1].lower()])
        if stack[-1].lower() not in operators and stack[-1].lower() not in alias and not stack[-1].isdigit():
            raise ValueError
        if not len(stack) > 1:
            raise StackUnderflowError
        if stack[-1].lower() == "dup":
            if stack[-2].isdigit():
                return process(stack[:-2] + [stack[-2]] * 2)
            substack = process(stack[:-1])
            return substack[:-1] + [substack[-1]] * 2
        if stack[-1].lower() == "drop":
            return process(stack[:-2])
        if all(element.isdigit() for element in stack):
            return [int(element) for element in stack]
        if not len(stack) > 2:
            raise StackUnderflowError
        if stack[-1].lower() == "over":
            return process(stack[:-1] + [stack[-3]])
        if stack[-1].lower() == "swap":
            return process(stack[:-3] + [stack[-2]] + [stack[-3]])
        if stack[-1] == '+':
            return process(stack[:-2]) + int(stack[-2])
        if stack[-1] == '-':
            return process(stack[:-2]) - int(stack[-2])
        if stack[-1] == '/':
            return process(stack[:-2]) // int(stack[-2])
        if stack[-1] == '*':
            return process(stack[:-2]) * int(stack[-2])

    operators = ['+', '-', '/', '*', 'dup', 'drop', 'over', 'swap']
    clean_stack = []
    alias = dict()
    for string in input_data:
        if string.startswith(':'):
            words = string.split()
            name, replacement = words[1], words[2:-1]
            if name.isdigit():
                raise ValueError
            alias[name.lower()] = replacement
        else:
            for word in string.split():
                clean_stack.append(word)
    clean_stack = process(clean_stack)
    return clean_stack if type(clean_stack) is list else [clean_stack]
