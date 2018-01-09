import re
from collections import Counter


def word_count(sentence):
    word_counter = Counter()
    split_sentence = re.split(r"[^a-zA-Z0-9']", sentence.lower().replace('.', '').replace(':', ''))
    for word in filter(None, split_sentence):
        word_counter[word.strip("'")] += 1

    return dict(word_counter)
