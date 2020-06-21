#!/usr/bin/env python3
"""tests for mrna.py"""

import os
from subprocess import getstatusoutput

prg = './mrna.py'


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

    protein = open('rosalind_mrna.txt').read().rstrip()
    rv, out = getstatusoutput(f'{prg} {protein}')
    assert rv == 0
    assert out.rstrip() == '448832'
