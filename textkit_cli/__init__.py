import argparse

import textkit

_COMMANDS = {
    "squeeze": textkit.collapse_spaces,
}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="textkit_cli")
    subparsers = parser.add_subparsers(dest="command")
    for name in _COMMANDS:
        subparsers.add_parser(name).add_argument("text")
    args = parser.parse_args(argv)
    print(_COMMANDS[args.command](args.text))
    return 0
