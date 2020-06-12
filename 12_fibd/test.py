#!/usr/bin/env python3
"""tests for fibd.py"""

from subprocess import getstatusoutput
import os

prg = './fibd.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    rv, out = getstatusoutput(prg)
    assert rv > 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_01():
    """runs"""

    rv, out = getstatusoutput(f'{prg} 6 3')
    assert rv == 0
    assert out == '4'


# --------------------------------------------------
def test_02():
    """runs"""

    rv, out = getstatusoutput(f'{prg} 88 17')
    assert rv == 0
    assert out == '1090086281966822291'


# --------------------------------------------------
def test_03():
    """runs"""

    rv, out = getstatusoutput(f'{prg} 83 18')
    assert rv == 0
    assert out == '98682772786101696'
