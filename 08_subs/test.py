#!/usr/bin/env python3
"""tests for subs.py"""

from subprocess import getstatusoutput, getoutput
import os

prg = './subs.py'


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
def test_input1():
    """good input"""

    rv, out = getstatusoutput(f'{prg} GATATATGCATATACTT ATAT')
    assert rv == 0
    assert out == '2 4 10'


# --------------------------------------------------
def test_input2():
    """good input"""

    seq, sub = open('rosalind_subs.txt').read().split()
    expected = open('rosalind_subs.out').read().rstrip()
    rv, out = getstatusoutput(f'{prg} {seq} {sub}')
    assert rv == 0
    assert out.rstrip() == expected
