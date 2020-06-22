#!/usr/bin/env python3
"""Find ORFs"""

import argparse
from itertools import takewhile
from Bio import Seq, SeqIO
from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find ORFs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input FASTA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(lambda s: str(s.seq), SeqIO.parse(args.file, 'fasta')))

    if not seqs:
        sys.exit(f'"{args.file.name}" contains no sequences.')

    rna = seqs[0].replace('T', 'U')
    orfs = set()
    for seq in [rna, Seq.reverse_complement(rna)]:
        for i in range(3):
            # Transcribe/translate DNA->RNA->AA
            if aa := translate(seq[i:]):
                # Record distinct ORFs
                for orf in find_orfs(aa):
                    orfs.add(orf)

    print('\n'.join(sorted(orfs)))


# --------------------------------------------------
def find_orfs(aa: List[str]) -> List[str]:
    """Find ORFs in AA sequence"""

    orfs = []
    while 'M' in aa and 'Stop' in aa:
        start = aa.index('M')
        stop = aa.index('Stop')
        if start > stop:
            break

        orfs.append(''.join(aa[start:stop]))
        aa = aa[start + 1:]

    return orfs


# --------------------------------------------------
def test_find_orfs() -> None:
    """Test find_orfs"""

    aa = ['M', 'A', 'M', 'A', 'P', 'R', 'Stop']
    assert find_orfs(aa) == ['MAMAPR', 'MAPR']


# --------------------------------------------------
def translate(seq: str) -> List[str]:
    """Make a jazz noise here"""

    codon_to_aa = {
        'AAA': 'K',
        'AAC': 'N',
        'AAG': 'K',
        'AAU': 'N',
        'ACA': 'T',
        'ACC': 'T',
        'ACG': 'T',
        'ACU': 'T',
        'AGA': 'R',
        'AGC': 'S',
        'AGG': 'R',
        'AGU': 'S',
        'AUA': 'I',
        'AUC': 'I',
        'AUG': 'M',
        'AUU': 'I',
        'CAA': 'Q',
        'CAC': 'H',
        'CAG': 'Q',
        'CAU': 'H',
        'CCA': 'P',
        'CCC': 'P',
        'CCG': 'P',
        'CCU': 'P',
        'CGA': 'R',
        'CGC': 'R',
        'CGG': 'R',
        'CGU': 'R',
        'CUA': 'L',
        'CUC': 'L',
        'CUG': 'L',
        'CUU': 'L',
        'GAA': 'E',
        'GAC': 'D',
        'GAG': 'E',
        'GAU': 'D',
        'GCA': 'A',
        'GCC': 'A',
        'GCG': 'A',
        'GCU': 'A',
        'GGA': 'G',
        'GGC': 'G',
        'GGG': 'G',
        'GGU': 'G',
        'GUA': 'V',
        'GUC': 'V',
        'GUG': 'V',
        'GUU': 'V',
        'UAA': 'Stop',
        'UAC': 'Y',
        'UAG': 'Stop',
        'UAU': 'Y',
        'UCA': 'S',
        'UCC': 'S',
        'UCG': 'S',
        'UCU': 'S',
        'UGA': 'Stop',
        'UGC': 'C',
        'UGG': 'W',
        'UGU': 'C',
        'UUA': 'L',
        'UUC': 'F',
        'UUG': 'L',
        'UUU': 'F',
    }

    k = 3
    codons = map(lambda i: seq[i:i + k], range(0, len(seq), k))
    return list(map(lambda codon: codon_to_aa.get(codon, '-'), codons))


# --------------------------------------------------
def test_translate():
    """Test translate"""

    assert translate('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
                     ) == list('MAMAPRTEINSTRING') + ['Stop']


# --------------------------------------------------
def find_kmers(seq, k):
    """Find k-mers in string"""

    seq = str(seq)
    n = len(seq) - k + 1
    return list(map(lambda i: seq[i:i + k], range(n)))


# --------------------------------------------------
def test_find_kmers():
    """Test find_kmers"""

    assert find_kmers('', 1) == []
    assert find_kmers('ACTG', 2) == ['AC', 'CT', 'TG']
    assert find_kmers('ACTG', 3) == ['ACT', 'CTG']
    assert find_kmers('ACTG', 4) == ['ACTG']
    assert find_kmers('ACTG', 5) == []


# --------------------------------------------------
if __name__ == '__main__':
    main()
