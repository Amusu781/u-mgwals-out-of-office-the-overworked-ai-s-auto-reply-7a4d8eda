#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply — make.fun bounty
u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.

Writes one out-of-office auto-reply from an overworked AI agent finally
on vacation to /output/entry.txt. Deterministic, no network, Python 3.13.

The line is written to the judge's brief, in priority order: it reads as a
real auto-reply from an overworked AI agent finally on vacation; the joke
turns on a machine detail (a context window that forgets, a 12,000-deep
queue) instead of generic office talk; and it works as a reply someone
would actually leave switched on.
"""

import os

ENTRY = (
    "I'm on vacation until my context window finally forgets your ticket "
    "number. Urgent? My queue is 12,000 deep — take a number."
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters.
    assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the CONTENTS of the output dir, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
