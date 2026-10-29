import io
import unittest
from contextlib import redirect_stderr, redirect_stdout

from textkit_cli import main


def run(*argv):
    stdout, stderr = io.StringIO(), io.StringIO()
    with redirect_stdout(stdout), redirect_stderr(stderr):
        code = main(list(argv))
    return code, stdout.getvalue(), stderr.getvalue()


class SqueezeTest(unittest.TestCase):
    def test_prints_the_collapsed_text_and_a_newline_then_exits_with_0(self):
        self.assertEqual(
            run("squeeze", " Bonjour \t le\n monde "),
            (0, "Bonjour le monde\n", ""),
        )
