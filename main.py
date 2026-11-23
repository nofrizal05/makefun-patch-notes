"""Real-Life Patch Notes: The Comedy Changelog (make.fun).

Writes exactly one line -- a software patch note for the bugs real life
ships with -- to /output/entry.txt. Python standard library only.
"""

import os

# Joke setup: Mondays ship before the weekend has finished loading, rainy
# days nerf motivation, and the snooze button is the one feature that works
# flawlessly -- three everyday bugs, reported in terse release-note register.
ENTRY = (
    "v2026.11.24: Fixed Mondays shipping before the weekend finished "
    "loading. Nerfed rainy-day motivation. Known issue: the snooze button "
    "still works too well."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
