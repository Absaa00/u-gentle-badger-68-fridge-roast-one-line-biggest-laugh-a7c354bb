# Fridge Roast: One Line, Biggest Laugh (MIT, see LICENSE).
#
# Writes a single roast of a smart fridge to /output/entry.txt.
# Deterministic: no input, no clock, no randomness, no network.
# The same bytes are written on every run.
# Standard library only.

import os

ENTRY = (
    "My smart fridge's latest update turned ice into a subscription, "
    "its camera snitched on my 2 a.m. snacks, and it still can't keep "
    "lettuce alive past Tuesday."
)

# Self-gate: the competition caps the line at 200 characters and the
# gate refuses anything that is not one line of 1-200 characters.
# Fail loudly here instead of shipping an entry the gate would refuse.
if not 1 <= len(ENTRY) <= 200 or "\n" in ENTRY or not ENTRY.strip():
    raise SystemExit("entry must be one line of 1-200 characters")


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the characters as written.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
