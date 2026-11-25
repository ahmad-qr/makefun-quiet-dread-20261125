"""A code review approval with quiet existential dread.

Writes the comment to /output/entry.txt for make.fun's
"Two Days of Quiet Dread" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "Approved. The code works, the tests pass, and I have no idea why "
    "— merging before I understand it."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 140 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 140, "line must be 1-140 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
