import unittest

from textkit import word_count


class WordCountTest(unittest.TestCase):
    def test_counts_the_words_separated_by_whitespace(self):
        self.assertEqual(word_count("Bonjour le\tmonde"), 3)

    def test_runs_of_whitespace_and_whitespace_at_the_ends_make_no_word(self):
        self.assertEqual(word_count(" \n Bonjour \t\n  le  monde\t "), 3)

    def test_empty_or_blank_text_counts_zero_words(self):
        for text in ("", " \t\n "):
            with self.subTest(text=text):
                self.assertEqual(word_count(text), 0)
