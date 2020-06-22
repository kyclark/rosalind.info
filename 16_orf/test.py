#!/usr/bin/env python3
"""tests for orf.py"""

import os
from subprocess import getstatusoutput

prg = './orf.py'
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
    """ok"""

    rv, out = getstatusoutput(f'{prg} {input1}')
    out = '\n'.join(sorted(out.splitlines()))
    expected = '\n'.join(
        sorted([
            'M', 'MGMTPRLGLESLLE', 'MLLGSFRLIPKETLIQVAGSSPCNLS', 'MTPRLGLESLLE'
        ]))
    assert rv == 0
    assert out == expected
