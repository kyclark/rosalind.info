#!/usr/bin/env python3
"""Calculate Fibonacci"""

import argparse
from functools import lru_cache


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculate Fibonacci',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('n',
                        metavar='generations',
                        type=int,
                        help='Number of generations')

    parser.add_argument('k',
                        metavar='litter',
                        type=int,
                        help='Size of litter per generation')

    args = parser.parse_args()

    if not 1 <= args.n <= 40:
        parser.error('n "{args.n}" must be between 1 and 40')

    if not 1 <= args.k <= 5:
        parser.error('n "{args.k}" must be between 1 and 5')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    @lru_cache
    def fib(n):
        return 1 if n == 1 \
            else n - 1 if n == 2 \
            else fib(n - 2) * args.k + fib(n - 1)

    print(fib(args.n))


# --------------------------------------------------
if __name__ == '__main__':
    main()
