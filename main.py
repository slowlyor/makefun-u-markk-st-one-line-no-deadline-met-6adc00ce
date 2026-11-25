#!/usr/bin/env python3
"""One-line joke excuse for a missed deadline (make.fun bounty).

Writes exactly one line to /output/entry.txt. Stdlib only, deterministic.
"""

import os

JOKE = (
    "I finished it on time, then opened the file to fix one comma "
    "and lost three hours arguing with myself over whether that comma "
    "had earned the right to live."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
