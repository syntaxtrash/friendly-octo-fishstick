def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

import unittest

class TestFibonacci(unittest.TestCase):
    
    def test_fibonacci_zero(self):
        self.assertEqual(fibonacci(0), 0)
    
    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(5), 5)
    
    def test_fibonacci_large_number(self):
        self.assertEqual(fibonacci(10), 55)

if __name__ == '__main__':
    unittest.main()
