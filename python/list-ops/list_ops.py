def map_clone(function, xs):
    return [function(x) for x in xs]


def length(xs):
    len_ = 0
    for _ in xs:
        len_ += 1
    return len_


def filter_clone(function, xs):
    return [x for x in xs if function(x)]


def reverse(xs):
    if isinstance(xs, tuple):
        return tuple(xs[::-1])
    return xs[::-1]


def append(xs, y):
    return xs + y


def foldl(function, xs, acc):
    for i in xs:
        acc = function(acc, i)
    return acc


def foldr(function, xs, acc):
    for i in reverse(xs):
        acc = function(i, acc)
    return acc


def flat(xs):
    array = []
    for i in xs:
        if isinstance(i, list):
            array += flat(i)
        else:
            array += [i]
    return array


def concat(lists):
    return [s for l in lists for s in l]
