import unittest

from textkit import collapse_spaces


class CollapseSpacesTest(unittest.TestCase):
    def test_collapses_each_run_of_whitespace_into_one_space(self):
        self.assertEqual(collapse_spaces("Bonjour \t\n  le  monde"), "Bonjour le monde")

    def test_removes_whitespace_at_both_ends(self):
        self.assertEqual(collapse_spaces(" \n Bonjour le monde\t "), "Bonjour le monde")

    def test_empty_or_blank_text_gives_empty_text(self):
        for text in ("", " \t\n "):
            with self.subTest(text=text):
                self.assertEqual(collapse_spaces(text), "")
