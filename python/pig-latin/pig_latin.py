import re


def translate(sentence):
    def translate_word(word):
        if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
            return word + 'ay'
        if word.startswith('qu'):
            return word[2:] + 'quay'
        if word[1:].startswith('qu'):
            return word[3:] + word[0] + 'quay'
        if word.startswith('y'):
            return word[1:] + word[0] + 'ay'
        groups = re.split('([aeiouy])', word)
        return ''.join(groups[1:]) + groups[0] + 'ay'

    return ' '.join([translate_word(word) for word in sentence.split()])
