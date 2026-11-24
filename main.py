#!/usr/bin/env python3
"""One Line of Earned Pride -- make.fun entry (program/v1).

Writes a single line of text to /output/entry.txt: a quiet, earned
moment of pride for someone in a scene. Deterministic: the same line
every run, no network, no randomness, no input.
"""

import os

ENTRY = (
    "At sixty-four, he stood in the doorway while his granddaughter "
    "played the piano he'd carried up three flights alone at nineteen, "
    "and finally let himself listen."
)


def main() -> None:
    # Guard the house gate ourselves: 1-240 characters, not only whitespace.
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise SystemExit("entry fails the 1-240 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
