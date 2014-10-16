#!/usr/bin/env python

from __future__ import print_function
import sys

def main(argv):
    file = argv[0]
    print('file = ' + file)
    f = open(file, 'r')
    seq = f.read().strip()
    print('seq = ' + seq)
    count = {} 
    for char in list(seq):
        if not count.has_key(char):
            count[char] = 0

        count[char] += 1
    #map(lambda s: count[s] = count[s] + 1, list(seq))

    #count = map(lambda s: count[s] = count[s] + 1, list(seq))
    for base in list('ACGT'):
        print(count[base], end=' ')

    print('')

if __name__ == "__main__":
    main(sys.argv[1:])
