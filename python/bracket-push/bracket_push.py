closing_bracket = {'}': '{',
                   ']': '[',
                   ')': '('}


def check_brackets(brackets):
    open_brackets = []
    for bracket in brackets:
        if bracket in closing_bracket.values():
            open_brackets.append(bracket)
        else:
            if not open_brackets or not open_brackets.pop() == closing_bracket[bracket]:
                return False
    return not open_brackets
