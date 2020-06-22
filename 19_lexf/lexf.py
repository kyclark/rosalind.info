#!/usr/bin/env python3
"""Enumerating k-mers Lexicographically"""

import argparse
from itertools import combinations
from typing import NamedTuple, List


class Args(NamedTuple):
    alphabet: List[str]
    num: int


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Enumerating k-mers Lexicographically',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('alphabet',
                        metavar='str',
                        nargs='+',
                        help='Letters of the alphabet')

    parser.add_argument('-n',
                        '--num',
                        help='Length n of strings',
                        metavar='int',
                        type=int,
                        default=2)

    args = parser.parse_args()

    if not 0 < args.num <= 10:
        parser.error(f'--num "{args.num}" must be between 1 and 10')

    return Args(args.alphabet, args.num)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    combos = sorted(set(combinations(args.alphabet * args.num, args.num)))
    print('\n'.join(sorted(map(''.join, combos))))


# --------------------------------------------------
if __name__ == '__main__':
    main()
