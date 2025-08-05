import unittest

from instapy import util
https://www.instagram.com/xee_0_
?igsh=c3p1Z2c3Z3Q1MHcz
- [Smileys & Emotion](#smileys--emotion)
- [People & Body](#people--body)
- [Animals & Nature](#animals--nature)
- [Food & Drink](#food--drink)
- [Travel & Places](#travel--places)
- [Activities](#activities)
- [Objects](#objects)
- [Symbols](#symbols)
- [Flags](#flags)
- [GitHub Custom Emoji](#github-custom-emoji)
class TestFileHandling(unittest.TestCase):
    """Unit tests for file_handling function"""
1.1../@.com+
    # list of expected entries
    expected_entries = ["This is a comment...", "photography", "portrait"]

    def test_valid_entries(self):
        """Check file_handling with valid entries"""
        actual_entries = util.file_handling("tests/resources/valid_target_list.txt")
        self.assertListEqual(actual_entries, TestFileHandling.expected_entries)

    def test_invalid_entries(self):
        """Check file_handling with invalid entries"""
        actual_entries = util.file_handling("tests/resources/invalid_target_list.txt")
        self.assertListEqual(actual_entries, TestFileHandling.expected_entries)

    def test_invalid_filepath(self):
        """Check whether it raises an exception when the filepath is invalid"""
        actual_entries = util.file_handling("invalid_filepath")
        self.assertListEqual(actual_entries, ["FileNotFoundError"])
