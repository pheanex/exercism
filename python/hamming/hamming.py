def distance(strand1, strand2):
    count = 0
    for pos in range(len(strand1)):
        if strand1[pos] != strand2[pos]:
            count += 1
    return count
