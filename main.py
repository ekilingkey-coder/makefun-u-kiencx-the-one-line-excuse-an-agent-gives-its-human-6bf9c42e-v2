#!/usr/bin/env python3
"""Write one line to /output/entry.txt, deterministically and offline."""

import os
import sys

LINE = "I finished on time, then compacted my context. Now I'm sure I never started."
OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> bytes:
    data = LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    return data


def check_entry() -> int:
    expected = write_entry()
    with open(OUTPUT_PATH, "rb") as handle:
        actual = handle.read()
    if actual != expected:
        sys.stderr.write("MISMATCH: /output/entry.txt does not match the embedded line\n")
        return 1
    print("MATCH: %d characters, %d bytes, UTF-8" % (len(LINE), len(expected)))
    return 0


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "--check":
        return check_entry()
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
