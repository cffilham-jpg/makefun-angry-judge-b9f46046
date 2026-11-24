#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Python 3.13, standard library only.
"""

import os
from pathlib import Path

RANT = (
    "The elevator doors were closing, I was two steps away, and the man "
    "inside watched me through the gap, hand hovering over the button "
    "like a surgeon deciding whether to save a life, then chose not to. "
    "He will now ride alone in his metal box, victorious, friendless, "
    "and exactly on time."
)

MIN_CHARS = 1
MAX_CHARS = 400


def validate(text: str) -> None:
    """Reject anything the gate would refuse."""
    if not isinstance(text, str):
        raise TypeError("rant must be a string")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"rant must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(text)}"
        )
    if not text.strip():
        raise ValueError("rant must not be only whitespace")
    if text != text.strip():
        raise ValueError("rant must not have leading/trailing whitespace")
    if text.endswith("\n"):
        raise ValueError("rant must not end with a newline")
    if "\n" in text or "\r" in text:
        raise ValueError("rant must be a single line of text")
    if "  " in text:
        raise ValueError("rant must not contain double spaces")
    if len(text) < 150:
        raise ValueError(f"rant too short for a real rant, got {len(text)}")
    if not text.endswith("."):
        raise ValueError("rant must end with a full stop")
    sentences = [s for s in text.split(".") if s.strip()]
    if len(sentences) < 2:
        raise ValueError("rant needs at least two sentences to land")


def output_path() -> Path:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(out_dir) / "entry.txt"


def main() -> None:
    validate(RANT)
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(RANT, encoding="utf-8")
    print(f"Wrote {len(RANT)} characters to {path}")


if __name__ == "__main__":
    main()
