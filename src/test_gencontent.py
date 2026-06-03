import unittest

from gencontent import extract_title

class TestGenContent(unittest.TestCase):
    def test_normal_case(self):
        result = extract_title("# Hello")
        self.assertEqual(result, "Hello")

    def test_raises_exception(self):
        with self.assertRaises(Exception):
            extract_title("Hello")

    def test_wrong_level_heading(self):
        with self.assertRaises(Exception):
            extract_title("## Hello")

if __name__ == "__main__":
    unittest.main()