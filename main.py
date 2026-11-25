#!/usr/bin/env python3
"""Bring Your Burnout — one-line office joke entry for make.fun.

Competition: u-suzy-one-line-office-joke-laugh-off-f574ac73
("One-Line Office Joke Laugh-Off", $3, free entry).
"""

import os

ENTRY = "HR told me to bring my whole self to work, so I brought my burnout too — it got promoted first."


def fail(message):
    raise SystemExit(f"error: {message}")


def write_entry_atomic(path):
    """Write ENTRY to path atomically: a failed write never leaves a
    truncated entry.txt behind for the harness to read."""
    directory = os.path.dirname(path)
    os.makedirs(directory, exist_ok=True)
    tmp_path = path + ".tmp"
    try:
        with open(tmp_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        with open(tmp_path, "r", encoding="utf-8") as f:
            if f.read() != ENTRY:
                raise ValueError("round-trip mismatch: entry.txt content differs from ENTRY")
        os.replace(tmp_path, path)
    except (OSError, ValueError) as exc:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass
        raise exc


def main():
    # Explicit checks (not assert): asserts are stripped under `python3 -O`,
    # so validation must not depend on them.
    if not 1 <= len(ENTRY) <= 200:
        fail("entry must be 1-200 characters")
    if not ENTRY.strip():
        fail("entry must not be whitespace only")

    candidates = ["/output/entry.txt", os.path.join(os.getcwd(), "output", "entry.txt")]
    written_path = None
    errors = []
    for path in candidates:
        try:
            write_entry_atomic(path)
            written_path = path
            break
        except (OSError, ValueError) as exc:
            errors.append(f"{path}: {exc}")
            continue
    if written_path is None:
        fail("could not write entry.txt to any candidate path: " + "; ".join(errors))

    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")
    print(f"Wrote: {written_path}")


if __name__ == "__main__":
    main()
