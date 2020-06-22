#!/usr/bin/env python3
"""tests for lexf.py"""

import os
from subprocess import getstatusoutput

prg = './lexf.py'


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

    rv, out = getstatusoutput(f'{prg} -n 2 A C G T')
    assert rv == 0
    expected = '\n'.join('AA AC AG AT CA CC CG CT GA '
                         'GC GG GT TA TC TG TT'.split())
    assert out == expected


# --------------------------------------------------
def test_ok2():
    """runs ok"""

    expected_file = './expected.2.txt'
    assert os.path.isfile(expected_file)
    rv, out = getstatusoutput(f'{prg} -n 3 A B C D E F G H I')
    assert rv == 0
    assert out.rstrip() == open(expected_file).read().rstrip()


# --------------------------------------------------
def test_ok3():
    """runs ok"""

    expected_file = './expected.3.txt'
    assert os.path.isfile(expected_file)
    rv, out = getstatusoutput(f'{prg} -n 3 A B C D E F G H')
    assert rv == 0
    assert out.rstrip() == open(expected_file).read().rstrip()
