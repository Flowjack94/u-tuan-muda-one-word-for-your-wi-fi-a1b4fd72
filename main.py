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

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_WORD + "\n")

if __name__ == "__main__":
    main()
