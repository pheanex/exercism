def slices(string, size):
    if not 0 < size <= len(string):
        raise ValueError("Slice size not valid")
    slicelist = []
    for i in range(len(string)-size+1):
        slicelist.append(list([int(s) for s in string[i:i+size]]))
    return slicelist
