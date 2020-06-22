#!/usr/bin/env python3
"""Calculating Protein Mass"""

import argparse
from typing import NamedTuple


class Args(NamedTuple):
    protein: str


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Calculating Protein Mass',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('protein', metavar='str', help='Protein')

    args = parser.parse_args()

    return Args(args.protein)


# --------------------------------------------------
def main() -> None:
    """Make a jazz noise here"""

    args = get_args()

    print('{:0.3f}'.format(sum(map(mass, args.protein))))


# --------------------------------------------------
def mass(residue: str) -> float:
    """Return mass of residue"""

    mass = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }

    return mass.get(residue, 0)


# --------------------------------------------------
def test_mass() -> None:
    """Test mass"""

    assert mass('') == 0
    assert mass('0') == 0
    assert mass('A') == 71.03711
    assert mass('W') == 186.07931


# --------------------------------------------------
if __name__ == '__main__':
    main()
