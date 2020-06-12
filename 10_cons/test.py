#!/usr/bin/env python3
"""tests for cons.py"""

from subprocess import getstatusoutput, getoutput
import os

prg = './cons.py'
input1 = './inputs/1.fa'
output1 = './inputs/1.out'
input2 = './inputs/2.fa'
output2 = './inputs/2.out'


# --------------------------------------------------
def test_exists():
    """usage"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{prg} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def run(in_file, out_file):
    """runner"""

    rv, out = getstatusoutput(f'{prg} {in_file}')
    expected = open(out_file).read().rstrip()
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_input1():
    """good input"""

    run(input1, output1)
