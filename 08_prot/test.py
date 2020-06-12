#!/usr/bin/env python3
"""tests for rna.py"""

from subprocess import getstatusoutput, getoutput
import os

prg = './rna.py'


# --------------------------------------------------
def test_exists():
    """usage"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for arg in ['', '-h', '--help']:
        out = getoutput(f'{prg} {arg}')
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_input1():
    """good input"""

    rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
    rv, out = getstatusoutput(f'{prg} {rna}')
    assert rv == 0
    assert out == 'MAMAPRTEINSTRING'


# --------------------------------------------------
def test_input2():
    """good input"""

    rna = open('rosalind_prot.txt').read().rstrip()
    expected = open('rosalind_prot.out').read().rstrip()
    rv, out = getstatusoutput(f'{prg} {rna}')
    assert rv == 0
    assert out.rstrip() == expected
