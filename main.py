"""Everyday Things, Two Lines, Longer Run.

A two-line explanation of a toaster for a 10-year-old: the first line
uses a sunbed analogy, and the second line honestly says what the
analogy maps and what it leaves out.
"""

import os

ENTRY_TEXT = (
    "A toaster is a tiny sunbed where your bread lies down to get a tan from glowing wires, then pops up golden-brown.\n"
    "The sunbed maps lying flat under heat until you brown, but leaves out that real sunbeds never launch you into the air when you are done."
)

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    # Gate self-check: the entry must be 1-400 chars and not only whitespace.
    if not 1 <= len(ENTRY_TEXT) <= 400 or not ENTRY_TEXT.strip():
        raise ValueError(
            f"ENTRY_TEXT failed gate: {len(ENTRY_TEXT)} chars, "
            "must be 1-400 chars and not only whitespace"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
