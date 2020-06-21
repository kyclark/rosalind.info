#!/usr/bin/env python3
"""tests for mrna.py"""

import os
from subprocess import getstatusoutput

prg = './mrna.py'
input1 = './inputs/1.txt'
input2 = './inputs/2.txt'


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
    """ok"""

    rv, out = getstatusoutput(f'{prg} MA')
    assert rv == 0
    assert out.rstrip() == '12'


# --------------------------------------------------
def test_ok2():
    """ok"""

    rv, out = getstatusoutput(f'{prg} {input1}')
    assert rv == 0
    assert out.rstrip() == '448832'


# --------------------------------------------------
def test_ok3():
    """ok"""

    rv, out = getstatusoutput(f'{prg} {input2}')
    assert rv == 0
    assert out.rstrip() == '415872'
