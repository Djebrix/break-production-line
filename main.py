"""Break Production, Own It — one brutally honest postmortem line.

Writes the line to /output/entry.txt (or $ENTRY_OUTPUT_DIR/entry.txt).
Stdlib only, no network, fully deterministic.
"""

import os

# Why it lands: a concrete destructive act (dropped the prod database),
# a plausible-sounding reason (testing the backup), then the twist that
# the safety net never existed. Specific, first-person, no hedging,
# and the punchline is the last word.
LINE = "I dropped the prod database to test the backup. There was no backup."


def main() -> None:
    # Enforce the competition gate at write time: 1-200 chars, single line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
