#!/usr/bin/env python3
"""tests for splc.py"""

import os
from subprocess import getstatusoutput

prg = './splc.py'
input1 = './inputs/1.fa'
input2 = './inputs/2.fa'
input3 = './inputs/3.fa'


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

    rv, out = getstatusoutput(f'{prg} {input1}')
    assert rv == 0
    assert out == 'MVYIADKQHVASREAYGHMFKVCA'


# --------------------------------------------------
def test_ok2():
    """runs ok"""

    rv, out = getstatusoutput(f'{prg} {input2}')
    assert rv == 0
    assert out == ''.join([
        'MSLLMIYRRLQSDRHPLGFMASRRLFRRARLFNKFRYAREYAGIATRTSE',
        'WHWKRKAWLIISCYVTEISATALDTSLLCLASYGTKHEFMVPEFTTTTPH',
        'IGAESCTFFYQIKGRLCGKGRIRTLSGTLPVGFPCSPLVSIERLTFGDAS',
        'TRFAPLTSRRVPVTMADRRSCALLGTSVEYVHPACPLLAI'
    ])


# --------------------------------------------------
def test_ok3():
    """runs ok"""

    rv, out = getstatusoutput(f'{prg} {input3}')
    assert rv == 0
    assert out == ''.join([
        'MWTTAVIRSSKIGQLRNGPAEIIRPSAIFFLGRFCIGLGLLTVSTFGKLR',
        'VAESTSKFRLANVYKYLSSLVKTVNNHIARSLLGLDPLTPQPHGVWCLSR',
        'SGCGFEFKGCTLLIGRAILPRGGWVSKTGGCGRHYRISNNDRALRAPTVP', 'TSQVASMNPSIVE'
    ])
