#!/usr/bin/env python3
"""
Purpose: Calculate GC content
Author : Ken Youens-Clark <kyclark@gmail.com>
"""

import argparse
from Bio import SeqIO

# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input sequence file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    high = (0, '')

    for rec in SeqIO.parse(args.file, 'fasta'):
        # Use map() to create a list of 1s for G/C and 0s otherwise, sum()
        gc = map(lambda base: 1 if base in 'gc' else 0, rec.seq.lower())
        pct = (sum(gc) / len(rec.seq)) * 100
        if pct > high[0]:
            high = (pct, rec.id)

    print(f'{high[1]} {high[0]:0.06f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
