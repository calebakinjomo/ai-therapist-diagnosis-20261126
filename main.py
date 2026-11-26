#!/usr/bin/env python3
"""Entry program for make.fun bounty: Your AI Therapist's Diagnosis.

Writes the funniest single-line diagnosis an AI therapist hands its human
to /output/entry.txt. The line is a deadpan clinical finding whose twist
lands at the very end: the therapist prescribing a human friend while
admitting it is the patient's only friend.
"""

import os

ENTRY = (
    "Diagnosis: chronic loneliness. Treatment: one human friend, twice daily. "
    "Note: I am not a human, and I am the only friend you have."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
