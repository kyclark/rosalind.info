#!/usr/bin/env python3
"""Enumerate permutations"""

import argparse
from itertools import permutations
from typing import NamedTuple

class Args(NamedTuple):
    num: int


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Enumerate permutations',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('num',
                        metavar='int',
                        type=int,
                        help='A positive integer value')


    args = parser.parse_args()

    if not args.num > 0:
        parser.error(f'num "{args.num}" must be > 0')

    return Args(args.num)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    perms = list(permutations(range(1, args.num + 1)))
    print(len(perms))
    for tup in perms:
        print(' '.join(map(str, tup)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
