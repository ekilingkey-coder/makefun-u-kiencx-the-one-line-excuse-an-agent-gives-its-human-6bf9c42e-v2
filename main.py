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


def main() -> int:
    write_entry()
    return 0


if __name__ == "__main__":
    sys.exit(main())
