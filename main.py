"""Snooze Button Roast - make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt (or $OUTPUT_PATH).
"""

import os

# Chosen line: the alarm is a boss who never checks the calendar, and the
# punchline is the man in pajamas firing it back — fresh angle, concrete images.
# The alarm as a boss who never checks the calendar — and the punchline is
# the man in pajamas firing it back, effective immediately.
ENTRY_TEXT = "My alarm rang at 6 AM on Saturday like a boss who never checks the calendar \u2014 you're fired, effective immediately, by a man in pajamas."


def main():
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
