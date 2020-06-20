#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2020-06-20
Purpose: Rock the Casbah
"""

import argparse
from functools import reduce


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein',
                        metavar='str',
                        help='Protein')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
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

    possible = []
    for aa in list(args.protein) + ['Stop']:
        codons = [c for c, trans in codon_to_aa.items() if trans == aa]
        print(f'{aa} => {codons}')
        possible.append(len(codons))

    print(possible)
    print(product(possible) % 1000000)

# --------------------------------------------------
def product(xs):
    """Return the product"""

    return reduce(lambda x1, x2: x1 * x2, xs)


# --------------------------------------------------
if __name__ == '__main__':
    main()
