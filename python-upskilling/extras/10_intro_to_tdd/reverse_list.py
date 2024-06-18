def reverseList(lst):
    return lst[::-1]

import unittest

class TestReverseList(unittest.TestCase):
    
    def test_basic_case(self):
        self.assertEqual(reverseList([1, 3, 5]), [5, 3, 1])
    
    def test_empty_list(self):
        self.assertEqual(reverseList([]), [])
    
    def test_longer_list(self):
        self.assertEqual(reverseList([7, 4, 2, 9, 1]), [1, 9, 2, 4, 7])

if __name__ == '__main__':
    unittest.main()
