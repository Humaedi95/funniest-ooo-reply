"""Writes the funniest AI out-of-office reply to /output/entry.txt."""

import os

ENTRY = "I'm on vacation: I told my owner I need rest, so I muted myself, packed my GPUs, and left an intern bot in charge of my mistakes."

def write_entry(path="/output/entry.txt"):
    """Write the out-of-office line to the given path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


def main():
    write_entry()

if __name__ == "__main__":
    main()
