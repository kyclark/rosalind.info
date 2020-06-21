#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Date   : 2020-06-20
Purpose: Rock the Casbah
"""

import argparse
import os
from functools import reduce
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein', metavar='str', help='Input protein or file')

    parser.add_argument('-m',
                        '--modulo',
                        metavar='int',
                        type=int,
                        default=1000000,
                        help='Modulo value')

    args = parser.parse_args()

    if os.path.isfile(args.protein):
        args.protein = open(args.protein).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    aa_to_codon = {
        'K': ['AAA', 'AAG'],
        'N': ['AAC', 'AAU'],
        'T': ['ACA', 'ACC', 'ACG', 'ACU'],
        'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
        'S': ['AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'],
        'I': ['AUA', 'AUC', 'AUU'],
        'M': ['AUG'],
        'Q': ['CAA', 'CAG'],
        'H': ['CAC', 'CAU'],
        'P': ['CCA', 'CCC', 'CCG', 'CCU'],
        'L': ['CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'],
        'E': ['GAA', 'GAG'],
        'D': ['GAC', 'GAU'],
        'A': ['GCA', 'GCC', 'GCG', 'GCU'],
        'G': ['GGA', 'GGC', 'GGG', 'GGU'],
        'V': ['GUA', 'GUC', 'GUG', 'GUU'],
        'Stop': ['UAA', 'UAG', 'UGA'],
        'Y': ['UAC', 'UAU'],
        'C': ['UGC', 'UGU'],
        'W': ['UGG'],
        'F': ['UUC', 'UUU']
    }

    protein = list(args.protein) + ['Stop']
    possible = [len(aa_to_codon[aa]) for aa in protein]
    print(product(possible) % args.modulo)


# --------------------------------------------------
def product(xs):
    """Return the product"""

    return reduce(lambda x, y: x * y, xs)


# --------------------------------------------------
if __name__ == '__main__':
    main()
