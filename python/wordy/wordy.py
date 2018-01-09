def calculate(text):
    text = text.replace('plus', '+')
    text = text.replace('minus', '-')
    text = text.replace('multiplied by', '*')
    text = text.replace('divided by', '/')
    if not text.startswith('What is') or not text.endswith('?'):
        raise ValueError('Malformed question')
    text = text[len('What is'):-1].split()
    while len(text) > 2:
        try:
            text.insert(0, str(eval(''.join([text.pop(0), text.pop(0), text.pop(0)]))))
        except SyntaxError:
            raise ValueError('Invalid Input')
    if len(text) != 1:
        raise ValueError('Invalid Input')
    return int(float(text[0]))
