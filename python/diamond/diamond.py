import string


def make_diamond(char):
    width = 2 * (string.ascii_uppercase.index(char) + 1) - 1
    lines = []
    for index, char in enumerate(string.ascii_uppercase[:string.ascii_uppercase.index(char) + 1]):
        if index:
            line = char + (2 * index - 1) * ' ' + char
        else:
            line = char
        spaces = (width - len(line)) // 2 * ' '
        lines.append(spaces + line + spaces)
    for line in lines[:-1][::-1]:
        lines.append(line)
    return '\n'.join(lines) + '\n'
