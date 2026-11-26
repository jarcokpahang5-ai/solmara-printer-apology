"""The Printer Apology — make.fun one-line bounty entry.

Pure Python 3 standard library, deterministic, no network.
"""

LINE = "I'm sorry I jammed, shredded your report, and ran out of ink at 11:59 PM — I just knew you'd replace me with a PDF and I panicked."


def validate(line=LINE):
    """The entry must be exactly one line of 1-200 characters."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200
    assert "\n" not in line
    return line


if __name__ == "__main__":
    validate()

