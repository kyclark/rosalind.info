#!/usr/bin/env python3
"""tests for iprb.py"""

from subprocess import getstatusoutput, getoutput
import os

prg = './iprb.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for arg in ['', '-h', '--help']:
        out = getoutput(prg)
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_ok1():
    """ok"""

    rv, out = getstatusoutput(f'{prg} 2 2 2')
    assert rv == 0
    assert out == '0.78333'


# --------------------------------------------------
def test_ok2():
    """ok"""

    rv, out = getstatusoutput(f'{prg} 29 18 15')
    assert rv == 0
    assert out == '0.85286'
