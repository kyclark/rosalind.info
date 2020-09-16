#!/usr/bin/env python3

import argparse
import operator
from itertools import starmap, groupby
from typing import NamedTuple, List, Any, Tuple, Callable, Optional


class Args(NamedTuple):
    pi: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Longest Increasing Subsequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        'pi',
        metavar='int',
        type=int,
        nargs='+',
        help='Sequence of integers')

    args = parser.parse_args()


    return Args(args.pi)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()
    print(' '.join(map(str, lis(args.pi))))
    print(' '.join(map(str, reversed(lis(list(reversed(args.pi)))))))

# https://cp-algorithms.com/sequences/longest_increasing_subsequence.html
def lis(xs):
    n = len(xs)
    d = [1 for _ in xs]
    p = [-1 for _ in xs]
    for i in range(n):
        for j in filter(lambda j: j < i, range(n)):
            if xs[j] < xs[i] and d[i] < d[j] + 1:
                d[i] = d[j] + 1
                p[i] = j

    print('d', d)
    print('p', p)

    ans = d[0]
    pos = 0
    for i in range(n):
        if d[i] > ans:
            ans = d[i]
            pos = i

    print('ans', ans)
    print('pos', pos)

    subseq = []
    while pos != -1:
        subseq.append(xs[pos])
        pos = p[pos]

    return list(reversed(subseq))

main()
