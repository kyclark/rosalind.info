#!/usr/bin/env python3
"""tests for orf.py"""

import os
from subprocess import getstatusoutput

prg = './orf.py'
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
def run(file, expected):
    """run with inputs"""

    rv, out = getstatusoutput(f'{prg} {file}')
    assert rv == 0
    assert set(out.splitlines()) == set(expected)


# --------------------------------------------------
def test_ok1():
    """ok"""

    expected = [
        'M', 'MGMTPRLGLESLLE', 'MLLGSFRLIPKETLIQVAGSSPCNLS', 'MTPRLGLESLLE'
    ]

    run(input1, expected)


# --------------------------------------------------
def test_ok2():
    """ok"""

    expected = [
        'M', 'MAEGGYRTSNHGSSL', 'MAYPRQYVRCLPKW', 'MDARISTTFELPYLTICQAFTF',
        'MDKHKKWTPVFLLPLSCPISLSVRHLHSDG', 'MGLQ', 'MIDL', 'MLEAQTDG',
        'MLWTNTRNGRPYFYYL', 'MPARRPRFLLTQQERRRPAFARLLVVCQTVSLSSGETVECDSG',
        'MPCYGQTQEMDARISTTFELPYLTICQAFTF', 'MPDGFFVQWGNG', 'MPDR', 'MPFC',
        'MPNPEGWVDLVFHAFLLRQAVLGTRLSRRGGYNRKVPIRSSAAPCTSR',
        'MRLSRIALNRFPTGQRNRLAYDK', 'MSEETD', 'MTRMLEAQTDG',
        'MTTQKAGIQWAYNKLLTTAFGVTKLD', 'MVFWYTRR'
    ]

    run(input2, expected)


# --------------------------------------------------
def test_ok3():
    """ok"""

    expected = [
        'M', 'MACLAPRVPVS', 'MAIGVVWV', 'MANGVVATGLGRSLLA', 'MDRRAMAIGVVWV',
        'MKHAFRISFQANNCVWVN', 'MLAGHVGWP', 'MLFSAV', 'MLGGLNYG',
        'MLGYRLHRMRTIPRPRHESL',
        'MLHAHGGWNLRPLDYSQKASWIQILGSLLPVIKATQHVPRASIVLVGLR', 'MLRAY',
        'MNRCRFYIPPEMPTAEGYPHGEGPSTL',
        'MNVLALCYFLRFRTNRRPGGASEVAIDTYYYLHATACRWLLA',
        'MPSVSVFRQTIVCGSTKLLVITMNVLALCYFLRFRTNRRPGGASEVAIDTYYYLHATACRWLLA',
        'MPTAEGYPHGEGPSTL', 'MRMKHAFRISFQANNCVWVN', 'MRMVAGIYDRWIILRRLLGSKS',
        'MRTIPRPRHESL', 'MRVAFCCWHFGGYVKSTTIHVWALV', 'MSGPWYSPHPM',
        'MSIRVNGQRRGSDRIGPLPSCLIL', 'MSREHLLSW', 'MSSTSTLKGCYM',
        'MSWRYAIFCGLERIAAQEERRKLQSILIIICTQPPVDGYWRSLGIAIPRLRQ', 'MTSPEYRTSARA',
        'MVAGIYDRWIILRRLLGSKS',
        'MVITSSLVDPHTIVCLKTDTEGMLHAHGGWNLRPLDYSQKASWIQILGSLLPVIK' +
        'ATQHVPRASIVLVGLR', 'MVKALPPYEYTSKWPTAW'
    ]

    run(input3, expected)
