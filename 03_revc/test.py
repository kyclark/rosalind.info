#!/usr/bin/env python3
"""tests for transcribe.py"""

from subprocess import getstatusoutput
import os.path
import re
import string
import random
from shutil import rmtree

prg = './revc.py'
input1 = './inputs/input1.txt'
input2 = './inputs/input2.txt'
output1 = './inputs/output1.txt'
output2 = './inputs/output2.txt'


# --------------------------------------------------
def random_filename():
    """generate a random filename"""

    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


# --------------------------------------------------
def test_exists():
    """usage"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput('{} {}'.format(prg, flag))
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


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
