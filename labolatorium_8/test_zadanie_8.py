import unittest
from zadanie_8 import zadanie

class Test(unittest.TestCase):
    def test_nawias(self):
        self.assertEqual(zadanie("(((((((((((((()"), "() ")
        self.assertIsNone(zadanie("((((((("))
    def test_nawias_2(self):
        self.assertEqual(zadanie("(((((((((()))()))(()))))))))"), "(((((((((()))()))(())))))) ")
        self.assertIsNone(zadanie("))))))))))))))))))))))))))))))))))))))))))())"))

if __name__ == '__main__': unittest.main()