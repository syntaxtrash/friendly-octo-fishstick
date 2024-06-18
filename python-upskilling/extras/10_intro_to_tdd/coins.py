def coins(cents):
    quarters = cents // 25
    cents %= 25
    dimes = cents // 10
    cents %= 10
    nickels = cents // 5
    cents %= 5
    pennies = cents
    return [quarters, dimes, nickels, pennies]

import unittest

class TestCoins(unittest.TestCase):
    
    def test_basic_case(self):
        self.assertEqual(coins(87), [3, 1, 0, 2])
    
    def test_zero_cents(self):
        self.assertEqual(coins(0), [0, 0, 0, 0])
    
    def test_large_amount(self):
        self.assertEqual(coins(356), [14, 0, 1, 1])
    
    def test_some_nickels(self):
        self.assertEqual(coins(25), [1, 0, 0, 0])
    
    def test_exact_change(self):
        self.assertEqual(coins(41), [1, 1, 1, 1])

if __name__ == '__main__':
    unittest.main()
