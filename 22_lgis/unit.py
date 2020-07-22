import operator
from lgis import cmp, is_asc, is_desc, pairs, decimate, binary_search


# --------------------------------------------------
def test_cmp() -> None:
    """Test cmp"""

    # descending
    assert cmp((3, 2, 1), operator.gt)
    assert not cmp((3, 2, 1), operator.lt)

    # ascending
    assert cmp((1, 2, 3), operator.lt)
    assert not cmp((1, 2, 3), operator.gt)


# --------------------------------------------------
def test_is_asc():
    """Test is_asc"""

    assert is_asc((1, 2, 3))
    assert not is_asc((3, 2, 1))
    assert not is_asc((1, 3, 2))


# --------------------------------------------------
def test_is_desc():
    """Test subseq"""

    assert is_desc((3, 2, 1))
    assert not is_desc((1, 2, 3))
    assert not is_desc((3, 1, 2))


# --------------------------------------------------
def test_pairs():
    """ Test pairs """

    assert pairs([]) == []
    assert pairs([1]) == []
    assert pairs([1, 2]) == [(1, 2)]
    assert pairs([1, 2, 3]) == [(1, 2), (2, 3)]
    assert pairs([1, 2, 3, 4]) == [(1, 2), (2, 3), (3, 4)]
    assert pairs(['foo']) == []
    assert pairs(['foo', 'bar']) == [('foo', 'bar')]
    assert pairs(['foo', 'bar', 'baz']) == [('foo', 'bar'), ('bar', 'baz')]
    assert pairs(['foo', 'bar', 'baz', 'quux']) == [('foo', 'bar'),
                                                    ('bar', 'baz'),
                                                    ('baz', 'quux')]


# --------------------------------------------------
def test_binary_search() -> None:
    """Test binary_search"""

    assert binary_search([], 1) is None
    assert binary_search([1], 1) == 0
    assert binary_search([1, 2, 3], 4) is None
    assert binary_search([1, 2, 3], 2) == 1


# --------------------------------------------------
def test_decimate() -> None:
    """Test decimate"""

    assert decimate([]) == None
    assert decimate(range(4)) == None
    assert decimate(range(10)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert decimate(range(3457)) == [
        345, 690, 1035, 1380, 1725, 2070, 2415, 2760, 3105, 3450
    ]
