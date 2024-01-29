import unittest
from main import word_count
import sys
import os

# Add the directory containing main.py to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

class TestWordCount(unittest.TestCase):
    def test_basic(self):
        # Test with a basic input
        test_input = "test.txt"
        # Create a temporary file with test content
        with open(test_input, 'w') as file:
            file.write("Hello world. Hello again.")

        expected_output = {'hello': 2, 'world': 1, 'again': 1}
        self.assertEqual(word_count(test_input), expected_output)

    def test_case_insensitivity(self):
        # Test case insensitivity
        test_input = "test_case.txt"
        with open(test_input, 'w') as file:
            file.write("Hello hello HELLO")

        expected_output = {'hello': 3}
        self.assertEqual(word_count(test_input), expected_output)

    def test_punctuation(self):
        # Test punctuation handling
        test_input = "test_punctuation.txt"
        with open(test_input, 'w') as file:
            file.write("Hello, hello! How are you?")

        expected_output = {'hello': 2, 'how': 1, 'are': 1, 'you': 1}
        self.assertEqual(word_count(test_input), expected_output)

    def test_empty_file(self):
        # Test with an empty file
        test_input = "test_empty.txt"
        with open(test_input, 'w') as file:
            pass

        expected_output = {}
        self.assertEqual(word_count(test_input), expected_output)

    def test_file_not_found(self):
        # Test with a non-existent file
        test_input = "non_existent.txt"
        expected_output = "File not found."
        self.assertEqual(word_count(test_input), expected_output)

if __name__ == '__main__':
    unittest.main()
