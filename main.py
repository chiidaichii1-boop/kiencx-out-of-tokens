#!/usr/bin/env python3
"""Write the funniest one-line error message an AI agent shows when it
runs out of tokens mid-sentence, to entry.txt.

The line is a flat error message that turns into the joke by cutting
itself off mid-sentence, exactly like the failure it reports. It stays
under the 140-character gate and is fully deterministic: the same line
is written on every run.
"""

import os

LINE = "Error: out of tokens mid-sentence. The agent's last words were about to be\u2014"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
