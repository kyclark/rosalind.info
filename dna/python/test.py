#!/usr/bin/env python3
"""tests for dna.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './dna.py'
input1 = './inputs/input1.txt'
input2 = './inputs/input2.txt'
expected1 = '20 12 17 21'
expected2 = '196 231 237 246'


# --------------------------------------------------
def test_exists():
    """program exists"""

    assert os.path.exists(prg)


# --------------------------------------------------
def test_usage():
    """prints usage with no args or for help"""

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{prg} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_arg():
    """uses command-line arg"""

    for file, expected in [(input1, expected1), (input2, expected2)]:
        dna = open(file).read()
        rv, out = getstatusoutput(f'{prg} {dna}')
        assert rv == 0
        assert out == expected


# --------------------------------------------------
def test_file():
    """uses file arg"""

    for file, expected in [(input1, expected1), (input2, expected2)]:
        rv, out = getstatusoutput(f'{prg} {file}')
        assert rv == 0
        assert out == expected
