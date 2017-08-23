#!/usr/bin/env python3
"""Report tetranucleotide count"""

import sys
import os.path

def main():
    """do the thing"""
    if len(sys.argv) != 2:
        print("  Usage: {} DNA\n".format(sys.argv[0]))
        sys.exit(1)

    arg = sys.argv[1]
    dna = ""
    if (os.path.exists(arg)):
        f = open(arg, "r")
        dna = "".join(f.read().splitlines()) # make a string
    else:
        dna = arg

    count = dict()
    for letter in dna.upper():
        count[letter] = (count.get(letter) or 0) + 1

    counts = [str(count.get(x) or 0) for x in ['A', 'C', 'G', 'T']]
    print(" ".join(counts))

if __name__ == "__main__":
    main()
