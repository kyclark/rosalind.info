#!/usr/bin/env python3
"""tests for revc.py"""

from subprocess import getstatusoutput, getoutput
import os
import re

prg = './revc.py'
input1 = './inputs/input1.txt'
input2 = './inputs/input2.txt'
output1 = './inputs/output1.txt'
output2 = './inputs/output2.txt'


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
def test_no_args():
    """die on no args"""

    rv, out = getstatusoutput(prg)
    assert rv != 0
    assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_uppercase():
    """runs on good input"""

    rv, out = getstatusoutput(f'{prg} AAAACCCGGT')
    assert rv == 0
    assert out == 'ACCGGGTTTT'


# --------------------------------------------------
def test_lowercase():
    """runs on good input"""

    rv, out = getstatusoutput(f'{prg} aaaacccggt')
    assert rv == 0
    assert out == 'accgggtttt'


# --------------------------------------------------
def test_input1():
    """runs on good input"""

    rv, out = getstatusoutput(f'{prg} {input1}')
    expected = open(output1).read().rstrip()
    assert rv == 0
    assert out == expected


# --------------------------------------------------
def test_input2():
    """runs on good input"""

    rv, out = getstatusoutput(f'{prg} {input2}')
    expected = open(output2).read().rstrip()
    assert rv == 0
    assert out == expected
