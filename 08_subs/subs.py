#!/usr/bin/env python3
"""
Author : Ken Youens-Clark <kyclark@gmail.com>
Purpose: Find subsequences
"""

import argparse
import re
from Bio.Seq import Seq


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find subsequences',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='str', help='Sequence')

    parser.add_argument('subseq', metavar='str', help='Sub-sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq, subseq = args.seq, args.subseq

    # 1: str.find()
    # last = 0
    # found = []
    # while True:
    #     pos = seq.find(subseq, last)
    #     if pos == -1:
    #         break
    #     found.append(str(pos + 1))
    #     last = pos + 1

    # print(' '.join(found))

    # 2: str.index()
    # found = []
    # last = 0
    # while subseq in seq[last:]:
    #     last = seq.index(subseq, last) + 1
    #     found.append(str(last))
    #     print(last)

    # print(' '.join(found))

    # 3: ugly, moving towards L.C.
    # found = []
    # seen = set()
    # for pos in [seq.find(subseq, pos) for pos in range(len(seq) - len(subseq))]:
    #     if pos == -1:
    #         break

    #     if pos not in seen:
    #         found.append(str(pos + 1))
    #         seen.add(pos)

    # print(' '.join(found))

    # 4: Same as 3 but shorter, using set(), sorted(), map()/str()
    # pos = [seq.find(subseq, pos) for pos in range(len(seq) - len(subseq))]
    # print(' '.join(map(str, sorted(set([i + 1 for i in pos if i >= 0])))))

    # 5: Same as 4 but L.C. -> map()
    # pos = filter(
    #     lambda pos: pos > 0,
    #     map(lambda pos: seq.find(subseq, pos) + 1,
    #         range(len(seq) - len(subseq))))
    # print(' '.join(map(str, sorted(set(pos)))))

    # 6: sorted()/set() -> unique()

    # # slow version
    # def unique(xs):
    #     uniq = []
    #     for x in xs:
    #         if x not in uniq:
    #             uniq.append(x)
    #     return uniq

    # # version relying on sorted()
    # def unique(xs):
    #     uniq = []
    #     for x in sorted(xs):
    #         if not uniq or (uniq and uniq[-1] != x):
    #             uniq.append(x)
    #     return uniq

    # pos = filter(
    #     lambda pos: pos > 0,
    #     map(lambda pos: seq.find(subseq, pos) + 1,
    #         range(len(seq) - len(subseq))))
    # print(' '.join(map(str, unique(pos))))

    # 6: kmers
    # found = []
    # k = len(subseq)
    # for i, sub in [(i, seq[i:i+k]) for i in range(len(seq) - k + 1)]:
    #     if sub == subseq:
    #         found.append(str(i + 1))

    # print(' '.join(found))

    # 7: kmers/FP
    # k = len(subseq)
    # found = filter(
    #     lambda t: t[1] == subseq,
    #     map(lambda i: (i + 1, seq[i:i + k]), range(len(seq) - k + 1)))
    # print(' '.join(map(lambda t: str(t[0]), found)))

    # 8: Regex to handle overlaps
    # pattern = '(?=(' + args.subseq + '))'
    # found = []
    # for match in re.finditer(pattern, args.seq):
    #     found.append(str(match.start() + 1))
    # print(' '.join(found))

    # 9: Shorter
    # pattern = '(?=(' + args.subseq + '))'
    # found = [str(m.start() + 1) for m in re.finditer(pattern, args.seq)]
    # print(' '.join(found))

    # 10: L.C. -> map()
    pattern = '(?=(' + args.subseq + '))'
    matches = map(lambda m: str(m.start() + 1), re.finditer(pattern, args.seq))
    print(' '.join(matches))


# --------------------------------------------------
if __name__ == '__main__':
    main()
