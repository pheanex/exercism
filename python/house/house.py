verses = [('house that Jack built', ''),
          ('malt', 'lay in'),
          ('rat', 'ate'),
          ('cat', 'killed'),
          ('dog', 'worried'),
          ('cow with the crumpled horn', 'tossed'),
          ('maiden all forlorn', 'milked'),
          ('man all tattered and torn', 'kissed'),
          ('priest all shaven and shorn', 'married'),
          ('rooster that crowed in the morn', 'woke'),
          ('farmer sowing his corn', 'kept'),
          ('horse and the hound and the horn', 'belonged to')]


def verse(nr):
    return 'This is the ' + verse_recurse(nr)


def verse_recurse(nr):
    thing, verb = verses[nr]
    if nr == 0:
        return '{}.'.format(thing)
    return '{}\nthat {} the '.format(thing, verb) + verse_recurse(nr - 1)


def rhyme():
    return '\n\n'.join(verse(i) for i in range(12))
