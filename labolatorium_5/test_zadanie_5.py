from zadanie_5 import szukanie_iloczynu
#from zadanie_5 import fibonacci
import unittest

class Test(unittest.TestCase):
    def test_fib(self):
        self.assertEqual(szukanie_iloczynu(104), [8, 13])
        self.assertFalse(szukanie_iloczynu(7))
    def test_fib_2(self):
        self.assertEqual(szukanie_iloczynu(602070), [610, 987])
        # self.assertEqual(szukanie_iloczynu(10803704), [2584, 4181])
        # self.assertFalse(szukanie_iloczynu(10803705))
        # self.assertFalse(szukanie_iloczynu(10803705456444447))

if __name__ == '__main__': unittest.main()