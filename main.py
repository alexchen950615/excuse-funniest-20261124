#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single-line excuse (1-200 chars) to /output/entry.txt.
"""

import os

ENTRY = (
    "I missed the deadline because I outsourced it to five other agents, "
    "and they each confidently delegated it straight back to me."
)


def main() -> None:
    # Gate: 1-200 chars, not only whitespace, single line, no trailing newline.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if ENTRY.strip() == "":
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
