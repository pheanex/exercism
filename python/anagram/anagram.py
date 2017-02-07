def detect_anagrams(anagram, wordlist):
    returnlist = []
    anagram = anagram.lower()
    for word in wordlist:
        lword = word.lower()
        if lword == anagram:
            continue
        if sorted(lword) == sorted(anagram):
            returnlist.append(word)
    return returnlist
