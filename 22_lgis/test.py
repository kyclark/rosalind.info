#!/usr/bin/env python3
"""tests for lgis.py"""

import os
from subprocess import getstatusoutput

prg = './lgis.py'


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

    rv, out = getstatusoutput(f'{prg} -n 3 -p 5 1 4 2 3')
    assert rv == 0
    assert out.rstrip() == '1 2 3\n5 4 2'
