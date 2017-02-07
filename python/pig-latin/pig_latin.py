def translate(sentence):
    def translate_word(word):
        if set("aeiou").intersection(word[0]):
            return word + "ay"
        else:
            for index, letter in enumerate(word):
                if letter in "aeiou":
                    if word[0:index][-1] == "q":
                        return word[index+1:] + word[0:index+1] + "ay"
                    return word[index:] + word[0:index] + "ay"

    return ' '.join([translate_word(word) for word in sentence.split()])
