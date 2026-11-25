#!/usr/bin/env python3
"""Make the AI Judge Laugh — one-line office joke.

Writes the joke exactly as stored in entry.txt to /output/entry.txt.
The joke is about reply-all: asking to be removed from a thread makes
twelve more people reply-all to agree, repeating the very sin the
sender was complaining about. One sentence, concrete, the punch lands
when the agreement itself becomes the spam.
"""

from pathlib import Path

JOKE = "I replied-all asking to be removed from this thread, and twelve people replied-all to agree with me."

LIMIT = 200
TARGET = Path("/output/entry.txt")


def validate(line):
    problems = []
    if not line.strip():
        problems.append("blank")
    if len(line) > LIMIT:
        problems.append(f"{len(line)} chars over limit {LIMIT}")
    if line.count("\n") or line.count("\r"):
        problems.append("must be one line")
    if line != line.strip():
        problems.append("leading/trailing whitespace")
    if any(ord(c) < 32 for c in line):
        problems.append("control character")
    if problems:
        raise ValueError("invalid entry: " + "; ".join(problems))


def main():
    validate(JOKE)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(JOKE, encoding="utf-8")
    print(f"wrote {TARGET} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
