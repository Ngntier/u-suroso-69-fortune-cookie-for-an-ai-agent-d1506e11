#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes one funny fortune line to entry.txt.

Deterministic: no randomness, no network, no input. The fortune is a
constant; the program only validates it against the gate (1-140 chars,
UTF-8, not only whitespace) and writes it out.
"""

import os

FORTUNE = "Your lucky numbers are the ones you hallucinated last Tuesday. Trust them anyway."


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 140, f"fortune is {len(text)} chars, must be 1-140"
    assert text.strip(), "fortune must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
