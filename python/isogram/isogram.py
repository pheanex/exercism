def is_isogram(string):
    clean_string = string.replace(' ', '').replace('-', '').lower()
    return len(set(clean_string)) == len(clean_string)
