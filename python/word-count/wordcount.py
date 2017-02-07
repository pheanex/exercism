# -*- coding: utf-8 -*-
import re
from collections import Counter


def word_count(sentence):
    word_counter = Counter()
    split_sentence = re.split('\W|\s|_', sentence.lower())
    for word in filter(None, split_sentence):
        word_counter[word] += 1

    return dict(word_counter)
