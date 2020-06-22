#!/usr/bin/env python3
"""tests for revp.py"""

import os
from subprocess import getstatusoutput

prg = './revp.py'
input1 = './inputs/1.fa'
input2 = './inputs/2.fa'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    rv, out = getstatusoutput(prg)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_ok1():
    """runs ok"""

    rv, out = getstatusoutput(f'{prg} {input1}')
    assert rv == 0
    expected = set(
        ['4 6', '5 4', '6 6', '7 4', '17 4', '18 4', '20 6', '21 4'])
    assert set(out.splitlines()) == expected

# --------------------------------------------------
def test_ok2():
    """runs ok"""

    expected_file = input2 + '.out'
    assert os.path.isfile(expected_file)

    rv, out = getstatusoutput(f'{prg} {input2}')
    assert rv == 0

    expected = set(open(expected_file).read().splitlines())
    assert set(out.splitlines()) == expected
