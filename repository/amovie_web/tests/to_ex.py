import pytest
from unittest.mock import Mock

def add(x, y):
   return x + y

def test_add():
   result = add(2, 2)
   assert result == 4

def test_add_negative():
   result = add(-1, -1)
   assert result == -2


def divide(x, y):
   if y == 0:
      raise ValueError("Cannot divide by zero")
   return x/y

def test_divide():
   result = add(6, 2)
   assert result == 3

def test_divide_by_zero():
   try:
      divide(2, 0)
      assert False
   except ValueError:
      assert True

def test_divide_by_zero_for_pytest():
   with pytest.raises(ValueError):
      divide(10, 0)



