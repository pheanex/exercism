protein_to_codons = {
    'Methionine': ['AUG'],
    'Phenylalanine': ['UUU', 'UUC'],
    'Leucine': ['UUA', 'UUG'],
    'Serine': ['UCU', 'UCC', 'UCA', 'UCG'],
    'Tyrosine': ['UAU', 'UAC'],
    'Cysteine': ['UGU', 'UGC'],
    'Tryptophan': ['UGG'],
    'STOP': ['UAA', 'UAG', 'UGA']
}
codon_to_protein = dict((v, k) for k in protein_to_codons for v in protein_to_codons[k])


def of_codon(codon):
    if codon not in codon_to_protein:
        raise ValueError
    return codon_to_protein[codon]


def proteins(sequence):
    proteins_ = []
    for codon in map(of_codon, chunkstring(sequence, 3)):
        if codon == 'STOP':
            break
        proteins_.append(codon)
    return proteins_


def chunkstring(string, size):
    return [string[i:i + size] for i in range(0, len(string), size)]
