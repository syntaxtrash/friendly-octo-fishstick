def isPalindrome(word):
    return word == word[::-1]

import unittest

class TestIsPalindrome(unittest.TestCase):
    
    def test_basic_palindrome(self):
        self.assertTrue(isPalindrome("racecar"))
    
    def test_non_palindrome(self):
        self.assertFalse(isPalindrome("hello"))
    
    def test_empty_string(self):
        self.assertTrue(isPalindrome(""))
    
    def test_single_char(self):
        self.assertTrue(isPalindrome("a"))
    
    # should fail 
    def test_case_insensitive(self):
        self.assertTrue(isPalindrome("Madam"))

if __name__ == '__main__':
    unittest.main()
