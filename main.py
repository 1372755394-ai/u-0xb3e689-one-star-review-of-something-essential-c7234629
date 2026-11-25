#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes one deadpan one-star review of sleep to /output/entry.txt
(1-160 UTF-8 characters, a single line, not only whitespace).
No network, no input, deterministic.
"""

import os
from pathlib import Path

REVIEW = (
    "Sleep charges eight hours a night and still delivers me to work "
    "tired, like a subscription I cannot cancel."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = REVIEW.strip()
    assert 1 <= len(text) <= 160, f"review is {len(text)} characters"
    assert "\n" not in text, "review must be a single line"
    assert text.strip(), "review must not be only whitespace"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
