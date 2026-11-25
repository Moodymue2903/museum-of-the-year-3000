"""Museum of the Year 3000 — make.fun entry.

The program writes one museum label to /output/entry.txt, byte for byte.

The label was picked from 15 original candidates drafted by three agents
working three different angles (household ritual objects, tech objects,
public infrastructure), each ranked against the published judge brief.
The plunger label won the pick: it lands on first read, the misreading is
literally true (plunging is an exorcism motion), it reads deadpan like a
real museum label, and the object is fresh — none of the brief's examples.

The GLM blind test that was meant to confirm the pick could not run: the
chat.z.ai daily quota was exhausted when the test was attempted, so no GLM
verdict exists for this entry yet. The entry is built and held; the GLM
test should be retried when the quota resets, before any submission.
"""

import os
import sys

LINE = "Toilet plunger, c. 2023. Ceremonial staff of the Bathroom Clergy, raised each morning to exorcise the demons of the drain."

MAX_CHARS = 200

ENTRY_PATH = "/output/entry.txt"


def find_problems(line):
    """List every way the line breaks the entry rules (empty when it is fine)."""
    problems = []
    if not line.strip():
        problems.append("line is blank or only whitespace")
    if len(line) > MAX_CHARS:
        problems.append(
            f"line is {len(line)} characters, but the limit is {MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        problems.append("line must fit on one line")
    return problems


def write_entry(line, path=ENTRY_PATH):
    """Write the line to the entry file, creating its directory first."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)


def verify_written(line, path=ENTRY_PATH):
    """Return an error message unless the file reads back byte-identical."""
    with open(path, "rb") as f:
        back = f.read()
    if back != line.encode("utf-8"):
        return f"read back {len(back)} bytes, expected {len(line)}"
    return None


def fail(message):
    """Print an error and stop with a failing exit code."""
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    line = LINE.strip()
    problems = find_problems(line)
    if problems:
        fail("; ".join(problems))

    write_entry(line)
    error = verify_written(line)
    if error is not None:
        fail(error)

    print(f"wrote {len(line)} characters to {ENTRY_PATH}")


if __name__ == "__main__":
    main()
