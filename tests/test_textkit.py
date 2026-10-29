import unittest

import textkit


class TextkitTest(unittest.TestCase):
    def test_package_imports(self):
        self.assertIsNotNone(textkit)
