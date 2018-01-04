def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        raise ValueError('Strands not equally long')
    return sum(1 for i in range(len(strand1)) if strand1[i] != strand2[i])
