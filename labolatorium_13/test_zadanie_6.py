import unittest
from zadanie_6 import pascal_test

class Test(unittest.TestCase):
    def test_pascal(self):
        self.assertEqual(len(pascal_test(15)), 15)
        self.assertEqual(pascal_test(15), [1, 14, 91, 364, 1001, 2002, 3003, 3432, 3003, 2002, 1001, 364, 91, 14, 1])
    def test_pascal_2(self):
        self.assertIsNone(pascal_test(-1))
        self.assertIsNone(pascal_test(0))

if __name__ == '__main__': unittest.main()