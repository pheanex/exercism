class StackUnderflowError(Exception):
    pass


def evaluate(input_data):
    def process(words):
        if not any(words):
            return []
        if not len(words) > 0:
            raise StackUnderflowError('Word missing')
        last_word = words[-1].lower()
        if len(words) == 1 and last_word.isdigit():
            return int(last_word)
        if last_word in aliases:
            return process(words[:-1] + aliases[last_word])
        if last_word not in operators and not last_word.isdigit():
            raise ValueError('Unknown operator or word missing')
        if not len(words) > 1:
            raise StackUnderflowError('Word missing')
        if last_word == "dup":
            if words[-2].isdigit():
                return process(words[:-2] + [words[-2]] * 2)
            sub_stack = process(words[:-1])
            return sub_stack[:-1] + [sub_stack[-1]] * 2
        if last_word == "drop":
            return process(words[:-2])
        if all(element.isdigit() for element in words):
            return [int(element) for element in words]
        if not len(words) > 2:
            raise StackUnderflowError('Word missing')
        if last_word == "over":
            return process(words[:-1] + [words[-3]])
        if last_word == "swap":
            return process(words[:-3] + [words[-2]] + [words[-3]])
        if last_word == '+':
            return process(words[:-2]) + int(words[-2])
        if last_word == '-':
            return process(words[:-2]) - int(words[-2])
        if last_word == '/':
            return process(words[:-2]) // int(words[-2])
        if last_word == '*':
            return process(words[:-2]) * int(words[-2])

    stack = []
    aliases = dict()
    for string in input_data:
        if string.startswith(':'):
            words = string.split()
            name, replacement = words[1].lower(), words[2:-1]
            if name.isdigit():
                raise ValueError('Digit cannot be an operator')
            aliases[name] = replacement
        else:
            for word in string.split():
                stack.append(word)
    operators = ['+', '-', '/', '*', 'dup', 'drop', 'over', 'swap']
    operators += list(aliases)
    stack = process(stack)
    return stack if type(stack) is list else [stack]
