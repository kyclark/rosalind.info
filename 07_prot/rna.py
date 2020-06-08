#!/usr/bin/env python3
""" Translate DNA/RNA to proteins """

import argparse
from itertools import takewhile
from Bio.Seq import Seq


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
    # print(''.join(
    #     takewhile(
    #         lambda c: c != 'Stop',
    #         map(lambda c: codon_to_aa.get(c, '-'),
    #             map(lambda i: seq[i:i + k], range(0, len(seq), k))))))

    # 6: Seq
    print(str(Seq(args.seq).translate()).replace('*', ''))

# --------------------------------------------------
if __name__ == '__main__':
    main()
