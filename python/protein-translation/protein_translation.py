def of_codon(codon):
    CodonToPolypeptide = {'AUG': 'Methionine',
                          'UUU': 'Phenylalanine',
                          'UUC': 'Phenylalanine',
                          'UUA': 'Leucine', 
                          'UUG': 'Leucine',
                          'UCU': 'Serine',
                          'UCC': 'Serine',
                          'UCA': 'Serine',
                          'UCG': 'Serine',
                          'UAU': 'Tyrosine',
                          'UAC': 'Tyrosine',
                          'UGU': 'Cysteine',
                          'UGC': 'Cysteine',
                          'UGG': 'Tryptophan',
                          'UAA': 'STOP',
                          'UAG': 'STOP',
                          'UGA': 'STOP'}
    if codon not in CodonToPolypeptide:
        raise ValueError
    return CodonToPolypeptide[codon]


def of_rna(string):
    chunks = [string[i:i + 3] for i in range(0, len(string), 3)]
    polipeptides = []
    for chunk in chunks:
        if of_codon(chunk) == 'STOP':
            break
        polipeptides.append(of_codon(chunk))
    return polipeptides
