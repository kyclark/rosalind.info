#!/usr/bin/env python3
"""tests for mprt.py"""

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = './mprt.py'
input1 = './inputs/1.txt'
input2 = './inputs/2.txt'


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
def test_01():
    """runs"""

    rv, out = getstatusoutput(f'{prg} {input1}')
    expected = '\n'.join([
        'B5ZC00',
        '85 118 142 306 395',
        'P07204_TRBM_HUMAN',
        '47 115 382 409',
        'P20840_SAG1_YEAST',
        '79 109 135 248 306 348 364 402 485 501 614',
    ])
    assert rv == 0
    assert out.rstrip() == expected


# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
