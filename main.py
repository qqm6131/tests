import unittest
import function

class TestStringFunctions(unittest.TestCase):

    def test_is_string(self):
        self.assertTrue(function.is_string(""))
        self.assertFalse(function.is_string("Python"))

    def test_reverse_string(self):
        self.assertEqual(function.reverse_string("hello"), "olleh")
        self.assertEqual(function.reverse_string("Python"), "nohtyP")
        self.assertEqual(function.reverse_string("12345"), "54321")

    def test_is_palindrome(self):
        self.assertTrue(function.is_palindrome("Тропа налево повела на порт"))
        self.assertTrue(function.is_palindrome("race car"))
        self.assertFalse(function.is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(function.count_vowels("оловянный"), 4)
        self.assertEqual(function.count_vowels("Привет, Андрей"), 4)
        self.assertEqual(function.count_vowels("aeiou"), 5)

    def test_remove_duplicates(self):
        self.assertEqual(function.remove_first_occurrence("hello"), "helo")
        self.assertEqual(function.remove_first_occurrence("Python"), "Python")
        self.assertEqual(function.remove_first_occurrence("aabbcc"), "abc")

if __name__ == '__main__':
    unittest.main()