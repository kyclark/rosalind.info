#!/usr/bin/env python3
"""Longest Increasing Subsequence"""

import argparse
import operator
from itertools import combinations, starmap, takewhile
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
        # type=int,
        type=str,
        nargs='+',
        help='Sequence of integers')

    args = parser.parse_args()

    return Args(args.pi)


# --------------------------------------------------
def trending(xs: List[Any], op: Callable) -> Optional[List[Any]]:
    """trending"""

    ret = []

    for i in range(len(xs)):
        vals = [xs[i]]
        for j in range(i, len(xs)):
            if op(xs[i], xs[j]):
                vals.append(xs[j])
        ret.append(vals)

    return ret

    # def first_hit():
    #     for i in range(len(xs)):
    #         for j in range(1, len(xs)):
    #             if op(xs[i], xs[j]):
    #                 return i

    # if pos := first_hit():
    #     ret = [xs[pos]]
    #     for i in range(pos + 1, len(xs)):
    #         if op(ret[-1], xs[i]):
    #             ret.append(xs[i])
    #     return ret

    # return None


# --------------------------------------------------
def test_trending() -> None:
    """Test lgis"""

    xs = [5, 1, 4, 2, 3]
    assert trending(xs, operator.lt) == [[5], [1, 4, 2, 3], [4], [2, 3], [3]]
    assert trending(xs, operator.gt) == [[5, 1, 4, 2, 3], [1], [4, 2, 3], [2],
                                         [3]]


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()

    for op in [operator.lt, operator.gt]:
        maybe = []
        for t in trending(args.pi, op):
            print(op, len(t))
            # print(t)
            # for k in range(len(t), 0, -1):
            #     for c in combinations(t, k):
            #         if cmp(c, op):
            #             maybe.append(c)

        print(' '.join(map(str, longest(maybe))))

    # flip = lambda t: tuple(reversed(t))
    # print(args.pi)
    # pi = sorted(list(map(flip, enumerate(args.pi))))
    # rev = list(reversed(sorted(list(map(flip, enumerate(args.pi))))))
    # print(pi)
    # print(rev)

    # pos = list(map(snd, pi))
    # show = lambda xs: ' '.join(map(lambda i: str(args.pi[i]), xs))

    # print('asc pos', pos)
    # print(show(longest(stretch(pos, operator.lt))))


#    pos = list(reversed(pos))
#    print('des pos', pos)
#    print(show(longest(stretch(pos, operator.gt))))

# for op in [operator.lt, operator.gt]:
#     vals = longest(stretch(list(map(snd, pi)), op))
#     print(op, vals)
#     # print(' '.join(map(str, map(lambda i: fst(args.pi[i]), vals))))
#     print(' '.join(map(lambda i: str(args.pi[i]), vals)))

# Ascending
# print(list(map(fst, longest(pi))))
# print(' '.join(longest(pi)))

# pi = list(reversed(pi))
# print(' '.join(longest(pi)))

# print(list(map(fst, longest(pi))))

# num_pi = len(args.pi)
# deciles = [num_pi] if num_pi < 10 else decimate(args.pi)

# asc, desc = (), ()
# low = 0
# for high in deciles:
#     print(low, high)
#     if asc_ := lgis(args.pi, is_asc, low, high):
#         asc = asc_
#     if desc_ := lgis(args.pi, is_desc, low, high):
#         desc = desc_

#     low = high

#     if asc and desc:
#         break

# print(' '.join(map(str, asc)))
# print(' '.join(map(str, desc)))

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

# # --------------------------------------------------
# def lgis(xs: List[Any], f: Callable, low: int,
#          high: int) -> Optional[List[Any]]:
#     """Find LGIS up to max_ using function"""
#     def search(k: int):
#         """Return first combo that matches"""
#         for i, combo in enumerate(combinations(xs, k)):
#             print(f'k "{k}" i {i}', end='\r')
#             if f(combo):
#                 return combo

#     found = None
#     while low <= high:
#         mid: int = (low + high) // 2

#         # If we find a combo, see if we can find one longer
#         if combo := search(mid):
#             found = combo
#             low = mid + 1
#         # else move down
#         else:
#             high = mid - 1

#     return found

# --------------------------------------------------
def cmp(xs: Tuple[Any, ...], op: Callable) -> bool:
    """Return True if the all the pairs are True for the given operator"""

    return all(starmap(op, pairs(xs)))

# # --------------------------------------------------
# def is_asc(xs: Tuple[Any, ...]) -> bool:
#     """Return True if the numbers are in ascending order"""

#     return cmp(xs, operator.lt)

# # --------------------------------------------------
# def is_desc(xs: Tuple[Any, ...]) -> bool:
#     """Return True if the numbers are in descending order"""

#     return cmp(xs, operator.gt)

# --------------------------------------------------
def pairs(xs: Tuple[Any, ...]) -> List[Tuple[(Any, Any)]]:
    """ Create a list of pair/tuples from a list """

    return [(xs[i], xs[i + 1]) for i in range(0, len(xs) - 1)]

# # --------------------------------------------------
# def binary_search(xs: List[Any], x: Any) -> Optional[int]:
#     """Binary search for position of value"""

#     low: int = 0
#     high: int = len(xs) - 1

#     while low <= high:
#         mid: int = (low + high) // 2
#         if xs[mid] == x:
#             return mid
#         elif xs[mid] < x:
#             low = mid + 1
#         elif xs[mid] > x:
#             high = mid - 1

#     return None

# # --------------------------------------------------
# def decimate(xs: List[Any]) -> Optional[List[int]]:
#     """Divide into 10 equal parts"""

#     if size := len(xs) // 100:
#         return [size * i for i in range(1, 11)]

# # --------------------------------------------------
# def chain(xs: List[List[Any]]) -> List[Any]:
#     """My version of chain to flatten lists of unique values"""

#     ret = []

#     for x in xs:
#         for v in x:
#             if v not in ret:
#                 ret.append(v)

#     return ret

# # --------------------------------------------------
# def test_chain() -> None:
#     """Test chain"""

#     assert chain([]) == []
#     assert chain([[1, 2]]) == [1, 2]
#     assert chain([[1, 2], [2, 3]]) == [1, 2, 3]

# # --------------------------------------------------
# def stretch(xs: List[int], f: Callable) -> List[List[int]]:
#     """Find stretches of ints"""

#     print('xs', xs)
#     ret = []
#     last = []

#     for i in range(len(xs) - 1):
#         x, y = xs[i], xs[i + 1]
#         if f(x, y):
#             last.append([x, y])
#         elif last:
#             ret.append(chain(last))
#             last = []

#     if last:
#         ret.append(chain(last))

#     print('ret', ret)
#     return ret

# # --------------------------------------------------
# def test_stretch() -> None:
#     """Test stretch"""

#     assert stretch([], operator.lt) == []
#     assert stretch([1], operator.lt) == []
#     assert stretch([1, 2], operator.lt) == [[1, 2]]
#     assert stretch([1, 2, 3], operator.lt) == [[1, 2, 3]]
#     assert stretch([1, 3, 2], operator.gt) == [[3, 2]]
#     assert stretch([2, 3, 1, 0, 4, 5], operator.lt) == [[2, 3], [0, 4, 5]]
#     assert stretch([2, 3, 1, 0, 4, 5], operator.gt) == [[3, 1, 0]]

# --------------------------------------------------
def longest(xs: List[List[Any]]) -> List[Any]:
    """Return the longest list"""

    return sorted(xs, key=len)[-1] if xs else []

# # --------------------------------------------------
# def test_longest() -> None:
#     """Test longest"""

#     assert longest([]) == []
#     assert longest([[1]]) == [1]
#     assert longest([[2, 3], [1]]) == [2, 3]
#     assert longest([[1], [4, 5, 6], [2, 3]]) == [4, 5, 6]

# # --------------------------------------------------
# def fst(tup: Tuple[Any, Any]) -> Any:
#     """Return second of tuple"""

#     return tup[0]

# # --------------------------------------------------
# def test_fst() -> None:
#     """Test fst"""

#     assert fst(('foo', 'bar')) == 'foo'

# # --------------------------------------------------
# def snd(tup: Tuple[Any, Any]) -> Any:
#     """Return second of tuple"""

#     return tup[1]

# # --------------------------------------------------
# def test_snd() -> None:
#     """Test snd"""

#     assert snd(('foo', 'bar')) == 'bar'

# --------------------------------------------------
if __name__ == '__main__':
    main()
