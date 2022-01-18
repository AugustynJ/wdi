import pytest
from zadanie_8 import zadanie

def test_nawias():
    assert zadanie("((())())()))") == "((())()) () "
def test_nawias_2():
    assert zadanie(")))))))))))))))))(((((((((((((((((((((((((((((((((((((((((((((((") == None
    assert zadanie("(((()") == None

test_nawias()
test_nawias_2()