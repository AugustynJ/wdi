import pytest
from zadanie_5 import szukanie_iloczynu

def test_fib():
    assert szukanie_iloczynu(9) == False
def test_fib_2():
    # assert szukanie_iloczynu(111112222223333344444455555) == False
    assert szukanie_iloczynu(10803704) == [2584, 4181]

test_fib()
test_fib_2()