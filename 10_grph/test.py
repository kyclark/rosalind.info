#!/usr/bin/env python3
"""tests for grph.py"""

from subprocess import getstatusoutput
import os
import random
import re
import string
import sys
import grph

prg = './grph.py'
sample1 = './inputs/1.fa'
sample2 = './inputs/2.fa'
sample3 = './inputs/3.fa'


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
def random_string():
    """Generate a random string"""

    return ''.join(
        random.sample(string.ascii_letters + string.digits,
                      k=random.randint(5, 10)))


# --------------------------------------------------
def test_bad_k():
    """bad k"""

    k = random.choice(range(-10, 1))
    rv, out = getstatusoutput(f'{prg} -k {k} {sample1}')
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f'-k "{k}" must be > 0', out)


# --------------------------------------------------
def test_bad_file():
    """usage"""

    bad = random_string()
    rv, out = getstatusoutput('{} {}'.format(prg, bad))
    assert rv != 0
    assert out.lower().startswith('usage:')
    assert re.search(f"No such file or directory: '{bad}'", out)



# --------------------------------------------------
def run_it(in_file, k):
    """run"""

    out_file = '.'.join([in_file, str(k), 'out'])
    assert os.path.isfile(out_file)

    expected = open(out_file).read().rstrip()
    cmd = '{} -k {} {} | sort'.format(prg, k, in_file)
    rv, out = getstatusoutput(cmd)
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def test_01():
    """runs ok"""

    run_it(sample1, 3)


# --------------------------------------------------
def test_02():
    """runs ok"""

    run_it(sample1, 4)


# --------------------------------------------------
def test_03():
    """runs ok"""
    run_it(sample1, 5)


# --------------------------------------------------
def test_04():
    """runs ok"""
    run_it(sample2, 3)


# --------------------------------------------------
def test_05():
    """runs ok"""
    run_it(sample2, 4)


# --------------------------------------------------
def test_06():
    """runs ok"""
    run_it(sample2, 5)


# --------------------------------------------------
def test_07():
    """runs ok"""
    run_it(sample3, 3)


# --------------------------------------------------
def test_08():
    """runs ok"""
    run_it(sample3, 4)


# --------------------------------------------------
def test_09():
    """runs ok"""
    run_it(sample3, 5)
