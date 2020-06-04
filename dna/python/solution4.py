#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Purpose: Tetranucleotide frequency
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='str', help='Input DNA sequence')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    count = {'a': 0, 'c': 0, 'g': 0, 't': 0}
    for base in args.dna.lower():
        if base in count:
            count[base] += 1

    print(' '.join([str(count.get(base, 0)) for base in 'acgt']))


# --------------------------------------------------
if __name__ == '__main__':
    main()
