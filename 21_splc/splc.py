#!/usr/bin/env python3
"""RNA Splicing"""

import argparse
import sys
from typing import NamedTuple, TextIO
from Bio import Seq, SeqIO


class Args(NamedTuple):
    file: TextIO


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='RNA Splicing',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input FASTA file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    args = parser.parse_args()

    return Args(args.file)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(lambda s: str(s.seq), SeqIO.parse(args.file, 'fasta')))

    if not seqs:
        sys.exit(f'"{args.file.name}" contains no sequences.')

    seq = seqs.pop(0)

    for intron in seqs:
        seq = seq.replace(intron, '')

    print(Seq.translate(seq.replace('T', 'U')).replace('*', ''))

# --------------------------------------------------
if __name__ == '__main__':
    main()
