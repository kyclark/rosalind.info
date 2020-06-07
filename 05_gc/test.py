#!/usr/bin/env python3
"""tests for gc.py"""

import os.path
import random
import string
import re
from subprocess import getstatusoutput, getoutput

prg = './gc.py'
sample1 = 'inputs/1.fa'
sample2 = 'inputs/2.fa'


# --------------------------------------------------
def test_exists():
    """ usage """

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """ usage """

    for flag in ['', '-h', '--help']:
        out = getoutput('{} {}'.format(prg, flag))
        assert re.match("usage", out, re.IGNORECASE)


# --------------------------------------------------
def test_bad_input():
    """ fails on bad input """

    bad = random_string()
    rv, out = getstatusoutput(f'{prg} {bad}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)


# --------------------------------------------------
def test_good_input1():
    """ works on good input """

    rv, out = getstatusoutput(f'{prg} {sample1}')
    assert rv == 0
    assert out == 'Rosalind_0808 60.919540'


# --------------------------------------------------
def test_good_input2():
    """ works on good input """

    rv, out = getstatusoutput(f'{prg} {sample2}')
    assert rv == 0
    assert out == 'Rosalind_5723 52.806415'


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
