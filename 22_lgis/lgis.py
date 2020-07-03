#!/usr/bin/env python3
"""Longest Increasing Subsequence"""

import argparse
from typing import NamedTuple, List


class Args(NamedTuple):
    n: int
    p: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Longest Increasing Subsequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        metavar='int',
                        type=int,
                        help='Positive integer')

    parser.add_argument('-p',
                        metavar='int',
                        type=int,
                        nargs='+',
                        help='Sequence of integers')

    args = parser.parse_args()

    return Args(args.n, args.p)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()

    for k in range(len(args.p), 0, -1):
        print(k)
        break

    print('done')

# --------------------------------------------------
def subseq(xs: List[int], k: int) -> List[List[int]]:
    """Find all possible subsequences of length k"""

    ret = []
end = len(xs) - k + 1
for start in range(0, end):
    for stop in range(i, end):
        print(xs[start:stop])
    for j in range(len(xs[k:])):
        print(i, j)
        ret.append([

# --------------------------------------------------
def test_subseq():
    """Test subseq"""

    assert subseq([], 1) == []
    assert subseq([1], 1) == [[1]]
    assert subseq([1, 2], 1) == [[1], [2]]
    assert subseq([1, 2], 2) == [[1, 2]]
    assert subseq([1, 2, 3], 2) == [[1, 2], [2, 3]]
    assert subseq([1, 2, 3], 3) == [[1, 2, 3]]


# --------------------------------------------------
if __name__ == '__main__':
    main()
