import pytest

from src.data.preprocessing_helpers import convert_to_int

def test_preprocessing_helpers():
    assert convert_to_int("2,456")==2456
