#!/usr/bin/env python3
"""Longest Increasing Subsequence"""

import argparse
import operator
from itertools import combinations, starmap
from typing import NamedTuple, List, Any, Tuple, Callable, Optional


class Args(NamedTuple):
    pi: List[int]


# --------------------------------------------------
def get_args() -> Args:
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Longest Increasing Subsequence',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pi',
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
    num_pi = len(args.pi)
    deciles = [num_pi] if num_pi < 10 else decimate(args.pi)

    asc, desc = (), ()
    low = 0
    for high in deciles:
        print(low, high)
        if asc_ := lgis(args.pi, is_asc, low, high):
            asc = asc_
        if desc_ := lgis(args.pi, is_desc, low, high):
            desc = desc_

        low = high

        if asc and desc:
            break

    print(' '.join(map(str, asc)))
    print(' '.join(map(str, desc)))


    # for k in deciles:
    #     for i, combo in enumerate(combinations(args.pi, k)):
    #         print(combo)
    #         print('{:78}'.format(f'k {k} i {i}'), end='\r')
    #         if is_asc(combo) and len(combo) > len(asc):
    #             print('Found asc!')
    #             print(combo)



    # len_pi = len(args.pi)
    # asc, desc = (), ()

    # k = len_pi
    # tried = set()

    # while True:
    #     print(f'k "{k}"')
    #     if k in tried:
    #         print(f'Already tried "{k}"')
    #         break

    #     tried.add(k)
    #     for i, combo in enumerate(combinations(args.pi, k)):
    #         print('{:78}'.format(f'k {k} i {i}'), end='\r')
    #         if is_asc(combo) and len(combo) > len(asc):
    #             print('Found asc!')
    #             asc = combo

    #         if is_desc(combo) and len(combo) > len(desc):
    #             print('Found desc!')
    #             desc = combo

    #     # if asc and desc:
    #     #     break

    #     if asc:
    #         k += int((len_pi - k) / 2)
    #     else:
    #         k = int(k / 2)

    #     while k in tried:
    #         k += 1 if asc else -1
    #         if k >= len_pi:
    #             break

    #     print(f'try k "{k}"')

    # print(args.pi)
    # for k in range(len(args.pi), 0, -1):
    #     print(f'k "{k}"')
    #     for i, combo in enumerate(combinations(args.pi, k)):
    #         print(k, i)
    #         if not asc and is_asc(combo):
    #             print('Found asc!')
    #             asc = combo

    #         if not desc and is_desc(combo):
    #             print('Found desc!')
    #             desc = combo

    #     if asc and desc:
    #         break


# --------------------------------------------------
def lgis(xs: List[Any], f: Callable, low: int, high: int) -> Optional[List[Any]]:
    """Find LGIS up to max_ using function"""

    def search(k: int):
        """Return first combo that matches"""
        for i, combo in enumerate(combinations(xs, k)):
            print(f'k "{k}" i {i}', end='\r')
            if f(combo):
                return combo

    found = None
    while low <= high:
        mid: int = (low + high) // 2

        # If we find a combo, see if we can find one longer
        if combo := search(mid):
            found = combo
            low = mid + 1
        # else move down
        else:
            high = mid - 1

    return found


# --------------------------------------------------
def cmp(xs: Tuple[Any, ...], op: Callable) -> bool:
    """Return True if the all the pairs are True for the given operator"""

    return all(starmap(op, pairs(xs)))


# --------------------------------------------------
def is_asc(xs: Tuple[Any, ...]) -> bool:
    """Return True if the numbers are in ascending order"""

    return cmp(xs, operator.lt)


# --------------------------------------------------
def is_desc(xs: Tuple[Any, ...]) -> bool:
    """Return True if the numbers are in descending order"""

    return cmp(xs, operator.gt)


# --------------------------------------------------
def pairs(xs: Tuple[Any, ...]) -> List[Tuple[(Any, Any)]]:
    """ Create a list of pair/tuples from a list """

    return [(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1)]


# --------------------------------------------------
def binary_search(xs: List[Any], x: Any) -> Optional[int]:
    """Binary search for position of value"""

    low: int = 0
    high: int = len(xs) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if xs[mid] == x:
            return mid
        elif xs[mid] < x:
            low = mid + 1
        elif xs[mid] > x:
            high = mid - 1

    return None


# --------------------------------------------------
def decimate(xs: List[Any]) -> Optional[List[int]]:
    """Divide into 10 equal parts"""

    if size := len(xs) // 100:
        return [size * i for i in range(1, 11)]


# --------------------------------------------------
if __name__ == '__main__':
    main()
