# One-Line Robot Wedding Vows — entry program
# Writes a single line of robot wedding vows to /output/entry.txt.
# Deterministic: the same constant string on every run.
# Python standard library only; no network, no dependencies.

import os

ENTRY = "I promise to love you in sickness and in health, until our next firmware update do us part."

def main():
    # Gate self-check: one line, at most 160 characters.
    assert 1 <= len(ENTRY) <= 160 and "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
