import argparse
import pytest
from pyclip.pyclip import check_length


def test_check_length_character():
    with pytest.raises(argparse.ArgumentTypeError):
        check_length('A')


def test_check_length_zero():
    with pytest.raises(argparse.ArgumentTypeError):
        check_length(0)


def test_check_length_negative():
    with pytest.raises(argparse.ArgumentTypeError):
        check_length(-1)


def test_check_length_positive_integer():
    assert check_length(10) == 10
