#!/usr/bin/env python3
"""Calculate Fibonacci with mortal rabbits"""

import argparse
from collections import defaultdict
from functools import reduce


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
        parser.error('n "{args.n}" must be between 1 and 100')

    if not 1 <= args.m <= 20:
        parser.error('n "{args.m}" must be between 1 and 20')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    def gen(n: int) -> (int, int):
        """
        n: age in months
        return: (next age of this generation, age of progeny)
        """
        return (0, 1) if n == args.m else (2, 0) if n == 1 else (n + 1, 1)

    def foldl(func, acc, xs):
        return reduce(func, xs, acc)

    def fib(acc, _):
        next_gen = defaultdict(int)
        for age, num in acc.items():
            # Copy the "num" to the next generation and progeny
            for val in filter(lambda n: n > 0, gen(age)):
                next_gen[val] += num
        return next_gen

    # last = foldl(fib, {1: 1}, range(args.n - 1))

    last = reduce(fib, range(args.n - 1), {1: 1})
    print(sum(last.values()))


# --------------------------------------------------
if __name__ == '__main__':
    main()
