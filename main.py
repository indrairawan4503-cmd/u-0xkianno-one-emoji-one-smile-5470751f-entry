#!/usr/bin/env python3
"""One Emoji, One Smile — Builder A.

Writes exactly one emoji (U+1F917 Hugging Face) to /output/entry.txt.
Deterministic: same bytes every run. No network, no randomness, no file
reads outside this repo.
"""

import os

EMOJI = "\U0001F917"  # 🤗 Hugging Face


def main() -> None:
    # Validate before writing: exactly one code point, 1-8 characters.
    assert len(EMOJI) == 1, "entry must be exactly one code point"
    assert EMOJI.strip() != "", "entry must not be only whitespace"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
