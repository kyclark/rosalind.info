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

    # print(product(possible) % 1000000)

    possible = pair(possible)
    print(possible)

    while len(possible) > 1:
        tmp = [p1 * p2 % 1000000 for p1, p2 in possible]
        possible = pair(tmp)

    last = possible.pop()
    print(last[0] * last[1] % 1000000)


# --------------------------------------------------
def pair(xs):
    """Create a list of pair/tuples from a list"""

    pairs = []
    while xs:
        if len(xs) == 1:
            pairs.append((xs.pop(0), 1))
        else:
            pairs.append((xs.pop(0), xs.pop(0)))

    return pairs


# --------------------------------------------------
def test_pair():
    """Test pair"""


    assert pair([]) == []
    assert pair([1]) == [(1, 1)]
    assert pair([1, 2]) == [(1, 2)]
    assert pair([1, 2, 3]) == [(1, 2), (3, 1)]
    assert pair([1, 2, 3, 4]) == [(1, 2), (3, 4)]


# --------------------------------------------------
def product(xs):
    """Return the product"""

    return reduce(lambda x1, x2: x1 * x2, xs)


# --------------------------------------------------
if __name__ == '__main__':
    main()
