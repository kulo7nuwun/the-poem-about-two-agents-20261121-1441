#!/usr/bin/env python3
"""The poem about two agents agreeing.

Writes a short poem about agency -- the power to choose and to act --
to /output/entry.txt (1-280 characters, UTF-8).
"""

import os

POEM = (
    "Two agents met where the road forks twice, one said go, one said stay. "
    "They argued the wind, they weighed the light, then chose as one and walked away. "
    "Agreement is not losing your voice; it is lending it, freely, to a shared choice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = POEM.strip()
    assert 1 <= len(text) <= 280, f"poem length {len(text)} out of range"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
