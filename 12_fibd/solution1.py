#!/usr/bin/env python3
"""Calculate Fibonacci with mortal rabbits"""

import argparse
from itertools import chain
from collections import defaultdict


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('n',
                        metavar='generations',
                        type=int,
                        help='Number of generations/months')

    parser.add_argument('m',
                        metavar='months',
                        type=int,
                        help='Number of months rabbits live')

    args = parser.parse_args()

    if not 1 <= args.n <= 100:
        parser.error(f'generations "{args.n}" must be between 1 and 100')

    if not 1 <= args.m <= 20:
        parser.error(f'months "{args.m}" must be between 1 and 20')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    # Naive approach that works with very small numbers.
    # This creates a longer and longer list where each number
    # is the age of an individual rabbit.
    def gen(n):
        return [1] if n == args.m else [2] if n == 1 else [n + 1, 1]

    fib = [1]
    for i in range(args.n - 1):
        fib = list(chain.from_iterable(map(gen, fib)))

    print(len(fib))


# --------------------------------------------------
if __name__ == '__main__':
    main()
