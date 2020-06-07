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
    seqs = []

    for rec in SeqIO.parse(args.file, 'fasta'):
        # Iterate each base and compare to G or C, add 1 to counter
        seq = rec.seq.lower()
        gc = 0

        for base in seq.lower():
            if base == 'g' or base == 'c':
                gc += 1
        pct = (gc / len(seq)) * 100

        seqs.append((pct, rec.id))

    high = sorted(seqs)[-1]
    print(f'{high[1]} {high[0]:0.06f}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
