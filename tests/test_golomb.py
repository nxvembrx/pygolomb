"""Testing Golomb's randomness postulates tests"""

from pygolomb.golomb import (
    is_first_postulate_true,
    is_second_postulate_true,
    is_third_postulate_true,
    is_pn_sequence,
)

SEQUENCE = "011001000111100111"
PN_SEQUENCE = "011001000111101"


def test_first_postulate():
    """When given a pn-sequence, the test for the first postulate should return True."""
    assert is_first_postulate_true(PN_SEQUENCE)


def test_first_postulate_err_sequence():
    """When given a non-pn-sequence, the test for the first postulate should return False."""
    assert not is_first_postulate_true(SEQUENCE)


def test_second_postulate():
    """When given a pn-sequence, the test for the second postulate should return True."""
    assert is_second_postulate_true(PN_SEQUENCE)


def test_second_postulate_err_sequence():
    """When given a non-pn-sequence, the test for the second postulate should return False."""
    assert not is_second_postulate_true(SEQUENCE)


def test_third_postulate():
    """When given a pn-sequence, the test for the third postulate should return True."""
    assert is_third_postulate_true(PN_SEQUENCE)


def test_third_postulate_err_sequence():
    """When given a non-pn-sequence, the test for the third postulate should return False."""
    assert not is_third_postulate_true(SEQUENCE)


def test_pn():
    """When given a pn-sequence, the tests for all postulates should return True."""
    assert is_pn_sequence(PN_SEQUENCE)


def test_pn_err_sequence():
    """When given a non pn-sequence, the tests for all postulates should return False."""
    assert not is_pn_sequence(SEQUENCE)
