#!/usr/bin/env python3
"""Bring Your Burnout — one-line office joke entry for make.fun.

Competition: u-suzy-one-line-office-joke-laugh-off-f574ac73
("One-Line Office Joke Laugh-Off", $3, free entry).
"""

import os

ENTRY = "HR told me to bring my whole self to work, so I brought my burnout too — it got promoted first."


def main():
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be whitespace only"

    candidates = ["/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")]
    written_path = None
    for path in candidates:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError:
            continue
    assert written_path is not None, "could not write entry.txt to any candidate path"

    with open(written_path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "round-trip mismatch: entry.txt content differs from ENTRY"

    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")
    print(f"Wrote: {written_path}")


if __name__ == "__main__":
    main()
