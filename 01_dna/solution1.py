#!/usr/bin/env python3
"""Tetranucleotide frequency"""

import argparse
import os
from typing import NamedTuple


class Args(NamedTuple):
    dna: str


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='str', help='Input DNA sequence')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    count_a, count_c, count_g, count_t = 0, 0, 0, 0

    for base in args.dna.lower():
        if base == 'a':
            count_a += 1
        elif base == 'c':
            count_c += 1
        elif base == 'g':
            count_g += 1
        elif base == 't':
            count_t += 1

    print(f'{count_a} {count_c} {count_g} {count_t}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
