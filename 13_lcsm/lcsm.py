#!/usr/bin/env python3
"""Longest Common Substring"""

import argparse
import sys
from Bio import SeqIO
import collections
from typing import Counter, List, NamedTuple, TextIO


class Args(NamedTuple):
    fasta: TextIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Longest Common Substring',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('fasta',
                        help='Input FASTA',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    args = parser.parse_args()

    return Args(args.fasta)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    seqs = list(map(lambda s: str(s.seq), SeqIO.parse(args.fasta, 'fasta')))

    if not seqs:
        sys.exit(f'"{args.fasta.name}" contains no sequences.')

    shortest = min(map(len, seqs))
    num_seqs = len(seqs)

    for i in range(shortest, 0, -1):
        subs : Counter[str] = collections.Counter()
        for kmer in map(lambda s: set(kmers(i, s)), seqs):
            subs.update(list(kmer))

        if mc := subs.most_common(1):
            most_common, num = mc[0]
            if num == num_seqs:
                print(most_common)
                break


# --------------------------------------------------
def kmers(k: int, seq: str) -> List[str]:
    """Find all substrings of a given length k"""

    return [seq[i:i + k] for i in range(len(seq) - k + 1)]


# --------------------------------------------------
def test_kmers() -> None:
    """Test kmers"""

    assert kmers(0, '') == ['']
    assert kmers(1, 'A') == ['A']
    assert kmers(1, 'AB') == ['A', 'B']
    assert kmers(2, 'AB') == ['AB']
    assert kmers(2, 'ABC') == ['AB', 'BC']


# --------------------------------------------------
if __name__ == '__main__':
    main()
