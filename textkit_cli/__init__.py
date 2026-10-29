import argparse

import textkit

_COMMANDS = {
    "squeeze": textkit.collapse_spaces,
}


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(prog="textkit_cli")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in _COMMANDS:
        subparsers.add_parser(name).add_argument("text")
    try:
        args = parser.parse_args(argv)
    except SystemExit as stop:
        return stop.code
    print(_COMMANDS[args.command](args.text))
    return 0
