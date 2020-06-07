m!/usr/bin/env python3
""" Hamming distance """

import argparse
from itertools import zip_longest, starmap
import operator


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Hamming distance',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='File inputs')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    line1, line2 = args.file.read().splitlines()[:2]

    # 1
    # # The base distance is the difference in their lengths
    # l1, l2 = len(line1), len(line2)
    # distance = abs(l1 - l2)

    # # Use the length of the shortest word
    # # Check the letters at each position
    # for i in range(min(l1, l2)):
    #     if line1[i] != line2[i]:
    #         distance += 1

    # print(distance)

    # 2
    # The base distance is the difference in their lengths
    #    distance = abs(len(line1) - len(line2))
    #
    #    # Use zip to pair up the letters
    #    for char1, char2 in zip(line1, line2):
    #        if char1 != char2:
    #            distance += 1
    #
    #    print(distance)

    # 3
    # distance = 0
    # for char1, char2 in zip_longest(line1, line2):
    #     if char1 != char2:
    #         distance += 1

    # print(distance)

    # 4
    # distance = [1 if char1 != char2 else 0
    #     for char1, char2 in zip_longest(line1, line2)]
    # print(sum(distance))

    # 5
    # distance = [
    #     1 for char1, char2 in zip_longest(line1, line2) if char1 != char2
    # ]
    # print(sum(distance))

    # 6
    # distance = filter(lambda t: t[0] != t[1], zip_longest(line1, line2))
    # print(len(list((distance))))

    # 7
    # distance = map(lambda t: t[0] != t[1], zip_longest(line1, line2))
    # print(sum((distance)))

    # 8
    # not_eq = lambda t: t[0] != t[1]
    # distance = map(not_eq, zip_longest(line1, line2))
    # print(sum((distance)))

    # 9
    distance = starmap(operator.ne, zip_longest(line1, line2))
    print(sum((distance)))


# --------------------------------------------------
if __name__ == '__main__':
    main()
