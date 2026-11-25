#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke.

The joke: asking to be removed from an email thread by replying-all,
only for twelve people to reply-all in agreement — the complaint itself
becomes the spam it was complaining about.

This script validates the single-line entry against the bounty gate
(one line, no more than 200 characters, no stray whitespace or control
characters) and writes it verbatim to /output/entry.txt.
"""

from pathlib import Path

JOKE = "I replied-all asking to be removed from this thread, and twelve people replied-all to agree with me."

LIMIT = 200
TARGET = Path("/output/entry.txt")


def problems(line):
    """Return a list of gate violations for one entry line."""
    found = []
    if not line.strip():
        found.append("blank entry")
    if len(line) > LIMIT:
        found.append(f"{len(line)} chars exceeds limit {LIMIT}")
    if "\n" in line or "\r" in line:
        found.append("must be a single line")
    if line != line.strip():
        found.append("leading/trailing whitespace")
    if "  " in line:
        found.append("double space")
    if any(ord(ch) < 32 for ch in line):
        found.append("control character present")
    return found


def validate(line):
    bad = problems(line)
    if bad:
        raise ValueError("invalid entry: " + "; ".join(bad))


def verify_written():
    """Read the output back and confirm it is byte-identical to the entry."""
    written = TARGET.read_text(encoding="utf-8")
    if written != JOKE:
        raise ValueError("written output differs from entry")


def main():
    validate(JOKE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(JOKE, encoding="utf-8")
    verify_written()
    print(f"wrote {TARGET} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
