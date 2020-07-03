#!/usr/bin/env python3
"""Tetranucleotide frequency"""

import argparse
import os
from typing import NamedTuple, Dict


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
    base = count(args.dna.upper())
    print(' '.join([str(count.get(base, 0)) for base in 'ACGT']))


# --------------------------------------------------
def count(dna) -> Dict[str, int]:
    """Count bases in DNA"""

    count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for base in dna:
        if base in count:
            count[base] += 1

    return count


# --------------------------------------------------
def test_count() -> None:
    """Test count"""

    assert count('') == {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    assert count('123XYZ') == {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    assert count('A') == {'A': 1, 'C': 0, 'G': 0, 'T': 0}
    assert count('C') == {'A': 0, 'C': 1, 'G': 0, 'T': 0}
    assert count('G') == {'A': 0, 'C': 0, 'G': 1, 'T': 0}
    assert count('T') == {'A': 0, 'C': 0, 'G': 0, 'T': 1}
    assert count('ACCGGGTTTT') == {'A': 1, 'C': 2, 'G': 3, 'T': 4}


# --------------------------------------------------
if __name__ == '__main__':
    main()
