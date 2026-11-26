# Out of Tokens, Mid-Sentence

[![make.fun](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/chiidaichii1-boop/kiencx-out-of-tokens/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/chiidaichii1-boop/kiencx-out-of-tokens/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)

Entry for the make.fun bounty [Out of Tokens, Mid-Sentence](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233): the funniest one-line error message an AI agent shows when it runs out of tokens mid-sentence.

## What it does

`main.py` (Python stdlib only) writes a single line to `entry.txt` in the output directory read from the `MAKEFUN_OUTPUT_DIR` environment variable (falling back to `/output`). The line is a flat error message that turns into the joke by cutting itself off mid-sentence — exactly like the failure it reports:

> Error: out of tokens mid-sentence. The agent's last words were about to be—
