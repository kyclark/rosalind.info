#!/usr/bin/env python3
"""tests for fib.py"""

from subprocess import getstatusoutput, getoutput
import os

prg = './fib.py'


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
def test_1():
    """runs on good input"""

    rv, out = getstatusoutput(f'{prg} 5 3')
    assert rv == 0
    assert out == '19'


# --------------------------------------------------
def test_2():
    """runs on good input"""

    rv, out = getstatusoutput(f'{prg} 30 4')
    assert rv == 0
    assert out == '436390025825'


# --------------------------------------------------
def test_3():
    """runs on good input"""

    rv, out = getstatusoutput(f'{prg} 29 2')
    assert rv == 0
    assert out == '178956971'
