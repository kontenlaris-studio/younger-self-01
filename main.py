"""One line to your younger self.

The line is the entry itself: one sentence an older self would send back
to the 3am version of them, no explanation attached.
"""

import os

LINE = "Your 3am idea isn't genius, it's the third coffee. Write it down anyway — the fourth one is."


def main():
    assert len(LINE) <= 200, "brief caps the line at 200 characters"
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
