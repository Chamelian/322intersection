"""
John Maynard
CSCI 332 Spring 2025
Programming Assignment #class17
I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by the university's academic integrity policy. I understand the importance the consequences of plagiarism.
"""

import unittest
from main import add_positive_integers

class TestMathFunctions(unittest.TestCase):
    def test_sum_correct(self):
        self.assertEqual(add_positive_integers(5, 10), 15)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            add_positive_integers(-1, 5)

    def test_wrong_type(self):
        with self.assertRaises(ValueError):
            add_positive_integers("5", 5) # type: ignore

if __name__ == "__main__":
    unittest.main()