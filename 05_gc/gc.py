#!/usr/bin/env python

import sys
from Bio import SeqIO

def main(file):
    sequences = []
    for record in SeqIO.parse(file, "fasta"):
        seq = record.seq
        sum_gc = (seq.count('G') + seq.count('C')) * 100
        gc = '%.6f' % float(float(sum_gc) / len(seq))
        sequences.append((record.id, gc))

    sequences.sort(key=lambda tup: tup[1], reverse=True)
    max = list(sequences.pop(0))
    print('\n'.join(max))

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print('Please provide a file argument')
        exit()

    main(args[1])
