#!/usr/bin/env python3
"""tests for lcsm.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './lcsm.py'
empty = './inputs/empty.fa'
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
def test_bad_file():
    """usage"""

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_empty():
    """dies on empty file"""

    rv, out = getstatusoutput(f'{prg} {empty}')
    assert rv != 0
    assert out == f'"{empty}" contains no sequences.'


# --------------------------------------------------
def test_short():
    """runs"""

    rv, out = getstatusoutput(f'{prg} {input1}')
    assert rv == 0
    assert out in ['AC', 'CA', 'TA']


# --------------------------------------------------
def test_long():
    """runs"""

    rv, out = getstatusoutput(f'{prg} {input2}')
    assert rv == 0
    assert out == ('GCCTTTTGATTTTAACGTTTATCGGGTGTAGTAAGATTGCG'
                   'CGCTAATTCCAATAAACGTATGGAGGACATTCCCCGT')


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
