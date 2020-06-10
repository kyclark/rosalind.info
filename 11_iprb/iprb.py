#!/usr/bin/env python3
""" Mendel's First Law """

import argparse
from scipy.special import comb


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('k',
                        metavar='dominant',
                        type=int,
                        help='Number of homozygous dominant')

    parser.add_argument('m',
                        metavar='heterozygous',
                        type=int,
                        help='Number of heterozygous')

    parser.add_argument('n',
                        metavar='recessive',
                        type=int,
                        help='Number of homozygous recessive')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    k, m, n = args.k, args.m, args.n

    # I don't actually understand this
    # Cf https://stackoverflow.com/questions/25119106/rosalind-mendels-first-law-iprb
    valid = comb(k, 2) + k * m + k * n + .5 * m * n + .75 * comb(m, 2)
    tot = comb(sum([k, m, n]), 2)
    print(f'{valid/tot:0.5f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
