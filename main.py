"""Firewall Rule Export — Export Windows Firewall rules to a text or CSV snapshot."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='firewall_rule_export',
        description='Export Windows Firewall rules to a text or CSV snapshot.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Firewall Rule Export')
    print('A readable dump of firewall rules.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
