#!/usr/bin/env python

from __future__ import print_function
import sys

def main(argv):
    input, pattern = argv[0:2]
    f = open(input, 'r')
    string = f.read().strip()
    print("string = " + string)

    pos = 0
    i = string.find(pattern, pos)
    if i > 0 :
        print("%s found at %s\n" % (pattern, i))
    else:
        print("%s not found\n" % pattern)

    if i = string.find(pattern, pos):
        print('true')
    else:
        print('false')

#    n = len(pattern)
#
#    for i in [0:len(string)-n]:
#        substr = string.


if __name__ == "__main__":
    main(sys.argv[1:])
