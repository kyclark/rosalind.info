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
def run(file, expected):
    """runs"""

    rv, out = getstatusoutput(f'{prg} {file}')
    assert out.rstrip() == expected

# --------------------------------------------------
def test_01():
    """runs"""

    expected = '\n'.join([
        'B5ZC00',
        '85 118 142 306 395',
        'P07204_TRBM_HUMAN',
        '47 115 116 382 409',
        'P20840_SAG1_YEAST',
        '79 109 135 248 306 348 364 402 485 501 614',
    ])
    run(input1, expected)

# --------------------------------------------------
def test_02():
    """runs"""

    expected = """
P13473_LMP2_HUMAN
32 38 49 58 75 101 123 179 229 242 257 275 300 307 317 356
P42098_ZP3_PIG
124 146 179 271
P80069_A45K_MYCBO
7 161
Q13VE3
95
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
P01042_KNH_HUMAN
48 169 205 294
P07204_TRBM_HUMAN
47 115 116 382 409
Q7S432
173
A3DF24
178
P07585_PGS2_HUMAN
211 262 303
Q9QSP4
196 250 326 443
    """.strip()
    run(input2, expected)

# --------------------------------------------------
def random_string():
    """ Generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))
