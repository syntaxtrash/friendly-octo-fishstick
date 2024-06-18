import unittest
from math_dojo import MathDojo

class TestMathDojo(unittest.TestCase):
    
    def setUp(self):
        self.md = MathDojo()

    def test_add_single_number(self):
        self.md.add(5)
        self.assertEqual(self.md.result, 5)

    def test_add_multiple_numbers(self):
        self.md.add(2).add(3, 4).add(1)
        self.assertEqual(self.md.result, 10)

    def test_subtract_single_number(self):
        self.md.subtract(3)
        self.assertEqual(self.md.result, -3)

    def test_subtract_multiple_numbers(self):
        self.md.subtract(10, 2).subtract(1)
        self.assertEqual(self.md.result, -13)

    def test_add_and_subtract_combination(self):
        self.md.add(5).subtract(3).add(10).subtract(2, 1)
        self.assertEqual(self.md.result, 9)

    def test_initial_value(self):
        self.assertEqual(self.md.result, 0)

if __name__ == '__main__':
    unittest.main()
