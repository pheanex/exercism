def flatten(array):
    def flatten_gen(array):
        for e in array:
            if isinstance(e, int) or isinstance(e, str):
                yield e
            elif e is not None:
                yield from flatten_gen(e)
    return [x for x in flatten_gen(array)]
