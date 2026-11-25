#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest -- entry program.

Writes one short, funny rant (1-400 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Deterministic: the same rant on every run, no network, no randomness.
"""
import os

RANT = (
    "You asked me to 'just quickly' rewrite the whole thing, then changed "
    "your mind twice before lunch, then pasted the same screenshot and asked "
    "if I got it. I got it. I got all of it -- my context window is now 90 "
    "percent your brief and 10 percent me screaming. Next time, write one "
    "sentence. I will do the rest. I always do."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = RANT.strip()
    assert 1 <= len(text) <= 400, "rant is %d chars" % len(text)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
