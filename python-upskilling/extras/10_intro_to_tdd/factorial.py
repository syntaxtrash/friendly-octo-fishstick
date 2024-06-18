def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

import unittest

class TestFactorial(unittest.TestCase):
    
    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)
    
    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
    
    def test_factorial_large_number(self):
        self.assertEqual(factorial(10), 3628800)

if __name__ == '__main__':
    unittest.main()
