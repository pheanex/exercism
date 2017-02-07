alphabet = "abcdefghijklmnopqrstuvwxyz"
table = str.maketrans(alphabet, alphabet[::-1])


def translate(text):
    text = ''.join([s.lower() for s in text if s.isalnum()])
    return text.translate(table)


def encode(text):
    text = translate(text)
    ciphertext_with_spaces = ""
    for i in range(0, len(text), 5):
        ciphertext_with_spaces += text[i:i+5] + " "
    return ciphertext_with_spaces.strip()


def decode(text):
    return translate(text)
