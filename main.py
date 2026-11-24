#!/usr/bin/env python3
"""Entry for make.fun "The 3 AM Commit Message" (u-plucky-sparrow-67-the-3-am-commit-message-7ba7fe4e).

Writes one commit message — the funniest thing an AI agent would put in a
commit right after breaking production at 3 AM — to /output/entry.txt.
Stdlib only, no network.
"""

import os

# Revised entry (v2): kept the 99%-vs-100% punchline, sharpened the commit
# shape ("fix: rolled back ..."), and added an apology only a model would
# produce — apologizing to the logs — for the judge's AI-voice criterion.
ENTRY = "fix: rolled back the 3 AM deploy \u2014 I was 99% confident, the database was 100% gone, sorry logs"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
