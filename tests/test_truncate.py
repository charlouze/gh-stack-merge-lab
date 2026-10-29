import unittest

from textkit import truncate


class TruncateTest(unittest.TestCase):
    def test_text_that_fits_is_returned_unchanged(self):
        self.assertEqual(truncate("Bonjour", 10), "Bonjour")

    def test_text_too_long_is_cut_and_ends_with_an_ellipsis(self):
        self.assertEqual(truncate("Bonjour le monde", 10), "Bonjour l…")

    def test_space_before_the_ellipsis_is_dropped(self):
        self.assertEqual(truncate("Bonjour le monde", 9), "Bonjour…")

    def test_width_below_one_is_rejected(self):
        for width in (0, -1):
            with self.subTest(width=width), self.assertRaises(ValueError):
                truncate("Bonjour", width)
