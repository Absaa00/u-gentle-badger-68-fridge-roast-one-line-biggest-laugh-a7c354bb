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


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts the characters as written.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
