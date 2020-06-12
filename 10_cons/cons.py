#!/usr/bin/env python3
"""Consensus sequence"""

import argparse
from collections import Counter, defaultdict
from pprint import pprint
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Consensus sequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input FASTA file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(lambda s: list(s.seq), SeqIO.parse(args.file, 'fasta')))
    consensus = ''
    cols = defaultdict(list)

    for col in zip(*seqs):
        counts = Counter(col)
        for base in 'ACGT':
            cols[base].append(counts.get(base, 0))
        commonest = counts.most_common(1)
        consensus += commonest[0][0] if commonest else ''

    print(consensus)
    for base in 'ACGT':
        print('{}: {}'.format(base, ' '.join(map(str, cols[base]))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
