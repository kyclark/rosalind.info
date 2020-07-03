#!/usr/bin/env python3
"""
Purpose: Calculate GC content
Author : Ken Youens-Clark <kyclark@gmail.com>
"""

import argparse
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from typing import Tuple


# --------------------------------------------------
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Calculate GC content',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input sequence file')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """ Make a jazz noise here """

    args = get_args()
    high = (0, '')

    # Using a list comprehension
    # high = sorted([gc(seq) for seq in SeqIO.parse(args.file, 'fasta')])[-1]

    # Using a map()
    high = sorted(map(gc, SeqIO.parse(args.file, 'fasta')))[-1]

    print(f'{high[1]} {high[0]:0.06f}')


# --------------------------------------------------
def gc(rec: SeqRecord) -> Tuple[(float, str)]:
    """ Return the GC content, record ID for a sequence """

    seq = str(rec.seq)
    gc = re.findall('[gc]', seq, re.IGNORECASE)
    length = len(seq)
    pct = (len(gc) / length) if length else 0
    return (pct, rec.id)


# --------------------------------------------------
def test_gc():
    """ Test gc """

    assert gc(SeqRecord(Seq(''), id='123')) == (0.0, '123')
    assert gc(SeqRecord(Seq('ACTG'), id='ABC')) == (.5, 'ABC')
    assert gc(SeqRecord(Seq('GGCC'), id='XYZ')) == (1.0, 'XYZ')


# --------------------------------------------------
if __name__ == '__main__':
    main()
