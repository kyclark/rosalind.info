#!/usr/bin/env python3
""" Translate DNA/RNA to proteins """

import argparse
from itertools import takewhile


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Translate RNA to proteins',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', type=str, metavar='str', help='RNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.seq.upper()
    codon_to_aa = {
        'UUU': 'F',
        'UUC': 'F',
        'UUA': 'L',
        'UUG': 'L',
        'UCU': 'S',
        'UCC': 'S',
        'UCA': 'S',
        'UCG': 'S',
        'UAU': 'Y',
        'UAC': 'Y',
        'UAA': 'Stop',
        'UAG': 'Stop',
        'UGU': 'C',
        'UGC': 'C',
        'UGA': 'Stop',
        'UGG': 'W',
        'CUU': 'L',
        'CUC': 'L',
        'CUA': 'L',
        'CUG': 'L',
        'CCU': 'P',
        'CCC': 'P',
        'CCA': 'P',
        'CCG': 'P',
        'CAU': 'H',
        'CAC': 'H',
        'CAA': 'Q',
        'CAG': 'Q',
        'CGU': 'R',
        'CGC': 'R',
        'CGA': 'R',
        'CGG': 'R',
        'AUU': 'I',
        'AUC': 'I',
        'AUA': 'I',
        'AUG': 'M',
        'ACU': 'T',
        'ACC': 'T',
        'ACA': 'T',
        'ACG': 'T',
        'AAU': 'N',
        'AAC': 'N',
        'AAA': 'K',
        'AAG': 'K',
        'AGU': 'S',
        'AGC': 'S',
        'AGA': 'R',
        'AGG': 'R',
        'GUU': 'V',
        'GUC': 'V',
        'GUA': 'V',
        'GUG': 'V',
        'GCU': 'A',
        'GCC': 'A',
        'GCA': 'A',
        'GCG': 'A',
        'GAU': 'D',
        'GAC': 'D',
        'GAA': 'E',
        'GAG': 'E',
        'GGU': 'G',
        'GGC': 'G',
        'GGA': 'G',
        'GGG': 'G'
    }

    k = 3

    # 1: for loop
    #    protein = ''
    #    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
    #        aa = codon_to_aa.get(codon, '-')
    #        if aa == 'Stop':
    #            break
    #        protein += aa

    # 2: list comprehension, slice to remove Stop
    # codons = [seq[i:i + k] for i in range(0, len(seq), k)]
    # aa = [codon_to_aa.get(codon, '-') for codon in codons]
    # if 'Stop' in aa:
    #     aa = aa[:aa.index('Stop')]
    # print(''.join(aa))

    # 3: L.C. -> map(), slice -> takewhile
    # codons = map(lambda i: seq[i:i + k], range(0, len(seq), k))
    # aa = map(lambda codon: codon_to_aa.get(codon, '-'), codons)
    # print(''.join(takewhile(lambda c: c != 'Stop', aa)))

    # 4: combine map()
    # aa = map(lambda c: codon_to_aa.get(c, '-'),
    #          map(lambda i: seq[i:i + k], range(0, len(seq), k)))
    # print(''.join(takewhile(lambda c: c != 'Stop', aa)))

    # 5: combine all
    print(''.join(
        takewhile(
            lambda c: c != 'Stop',
            map(lambda c: codon_to_aa.get(c, '-'),
                map(lambda i: seq[i:i + k], range(0, len(seq), k))))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
