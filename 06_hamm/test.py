#!/usr/bin/env python3
"""tests for hamming.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './hamm.py'
input1 = './inputs/1.txt'
input2 = './inputs/2.txt'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_bad_file():
    """Bad file"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def run(file, expected):
    """run on input"""

    rv, out = getstatusoutput(f'{prg} {file}')
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_input1():
    """input1"""

    run(input1, '7')


# --------------------------------------------------
def test_input2():
    """input2"""

    run(input2, '503')


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
