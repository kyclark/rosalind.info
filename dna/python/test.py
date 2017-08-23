#!/usr/bin/env python3
"""tests for dna.py"""

import os.path
from subprocess import getstatusoutput, getoutput
import re

script = "./dna.py"

def test_script_exists():
    """script is there"""
    assert os.path.exists(script)

def test_usage():
    """prints usage with no args"""
    (retval, out) = getstatusoutput(script)
    assert retval > 0
    assert re.search("usage", out, re.IGNORECASE)

def test_arg():
    """uses command-line arg"""
    dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
    out = getoutput("{} {}".format(script, dna)).rstrip()
    assert out == '20 12 17 21'

def test_file():
    """uses file arg"""
    out = getoutput("{} {}".format(script, "test.txt")).rstrip()
    assert out == '20 12 17 21'
