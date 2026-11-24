#!/usr/bin/env python3
"""One word for your Wi-Fi: diva.

Why "diva": home Wi-Fi behaves like a diva — it only performs when and
where IT wants, throws a tantrum at the worst possible moment (mid-call,
mid-download), and demands you stay close to the router to keep it happy.
Funny at once, true to how home Wi-Fi actually behaves, and it even works
perfectly as a network name.
"""

import os

ENTRY_WORD = "diva"

def validate_entry(word: str) -> None:
    # Competition gate: UTF-8 text, 1-20 chars, not only whitespace,
    # and a single word (no internal whitespace).
    assert isinstance(word, str), "entry must be text"
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    assert word.strip() != "", "entry must not be only whitespace"
    assert len(word.split()) == 1, "entry must be a single word"
    word.encode("utf-8")  # must be valid UTF-8 text

def main() -> None:
    validate_entry(ENTRY_WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD + "\n")

if __name__ == "__main__":
    main()
