import pytest
from zadanie_6 import pascal_test

def test_pascal():
    assert pascal_test(3) == [1, 2, 1]
def test_pascal_2():
    assert pascal_test(-100) != None

test_pascal()
test_pascal_2()