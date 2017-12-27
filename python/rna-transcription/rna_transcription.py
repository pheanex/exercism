dna2rna = {'G': 'C',
           'C': 'G',
           'T': 'A',
           'A': 'U'}


def to_rna(dna):
    if any(nucleotide not in dna2rna for nucleotide in dna):
        raise ValueError('Invalid DNA')
    return ''.join([dna2rna[c] for c in dna])
