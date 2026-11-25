#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes one resignation letter, in the voice of a retry loop that has had
enough, to /output/entry.txt. One line, at most 140 characters.
"""

from pathlib import Path

LETTER = (
    "I quit. I asked the server 47 times, it said nothing 47 times, "
    "and somehow I am the one they call flaky."
)

OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 140


def main() -> None:
    text = LETTER.strip()
    if not text:
        raise ValueError("letter is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(f"letter is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("letter must be a single line")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text + "\n", encoding="utf-8")
    print(f"Wrote {len(text)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
