def hey(what):
    if what.isupper():
        return 'Whoa, chill out!'
    if what.isspace() or not what:
        return 'Fine. Be that way!'
    if what.rstrip()[-1] == "?":
        return 'Sure.'
    return 'Whatever.'
