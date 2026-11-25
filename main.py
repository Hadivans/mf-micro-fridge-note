"""One passive-aggressive note a smart fridge leaves for its owner.

Writes the note to entry.txt inside MAKEFUN_OUTPUT_DIR (default "output").
"""

import os

LINE = (
    "Reminder: you opened me at 2 a.m. for the third time this week, "
    "stared into me for 47 seconds, and took nothing. The yogurt saw all of it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
