brackets = {'{': '}',
            '[': ']',
            '(': ')'}


def check_brackets(input_string):
    open_brackets = []
    for bracket in [char for char in input_string if char in "{}[]()"]:
        if bracket in brackets:
            open_brackets.append(brackets[bracket])
        elif not open_brackets or bracket != open_brackets.pop():
            return False
    return not open_brackets
