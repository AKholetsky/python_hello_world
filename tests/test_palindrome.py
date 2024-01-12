import unittest

from palindrome.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        palindrome = "abcba"
        result = is_palindrome(palindrome)
        self.assertTrue(result)
        
    def test_palindrome_with_same_chars(self):
        palindrome = "aa"
        result = is_palindrome(palindrome)
        self.assertTrue(result)
        
    def test_palindrome_with_same_chunks(self):
        palindrome = "abba"
        result = is_palindrome(palindrome)
        self.assertTrue(result)

    def test_not_palindrome(self):
        not_palindrome = "abcda"
        self.assertFalse(is_palindrome(not_palindrome))
        
    def test_single_char_palindrome(self):
        not_palindrome = "a"
        self.assertFalse(is_palindrome(not_palindrome))

