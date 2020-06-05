#!/usr/bin/env python3
""" Reverse complement """

import argparse
import os
from Bio import Seq


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Reverse complement',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq', metavar='str', help='Input sequence')

    args = parser.parse_args()

    if os.path.isfile(args.seq):
        args.seq = open(args.seq).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print(Seq.reverse_complement(args.seq))


# --------------------------------------------------
if __name__ == '__main__':
    main()
