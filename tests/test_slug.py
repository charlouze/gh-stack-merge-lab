import unittest

from textkit import slugify


class SlugifyTest(unittest.TestCase):
    def test_removes_accents_and_lowercases(self):
        self.assertEqual(slugify("ÉtÉ"), "ete")

    def test_collapses_a_run_of_separators_into_one_dash(self):
        self.assertEqual(slugify("à  la_mode!?2"), "a-la-mode-2")

    def test_never_starts_or_ends_with_a_dash(self):
        self.assertEqual(slugify("  Été à Paris !"), "ete-a-paris")

    def test_text_without_any_alphanumeric_gives_empty_slug(self):
        self.assertEqual(slugify(" -_!? "), "")
