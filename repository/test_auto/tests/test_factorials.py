# tests/test_factorials.py

import pytest
from main import factorials

def test_factorials():
    assert factorials(-1) is None
    assert factorials(0) == 1
    assert factorials(5) == 120

def test_factorials_invalid_input():
    with pytest.raises(TypeError):
        factorials(2.5)
