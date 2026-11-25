#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue — make.fun entry (program/v1).

Writes one monologue, spoken by a fantasy villain who is secretly just
very tired, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Python standard library only, deterministic, no network.
"""

import os

# The entry: "The Lich Accountant" — the dead will rise, after the ledgers.
ENTRY = (
    "Listen. I have ruled the Barrowlands for nine centuries, and tonight — "
    "tonight — the dead will rise. They will rise... after I finish these "
    "ledgers. Do you know how many souls crossed the river last quarter? "
    "Forty-one thousand. Each one needs a name, a cause, a signature. "
    "My throne — this magnificent, cursed throne — has a loose nail that "
    "has been stabbing my left cheek for two hundred years. The eclipse is "
    "coming. The eclipse can wait five minutes. I just need to sit here. "
    "Just — five minutes. The dead are patient. I taught them that."
)

MIN_CHARS = 1
MAX_CHARS = 600


def validate(text: str) -> None:
    """Gate validation, mirroring the sealed scorer:
    UTF-8 text, 1-600 characters, not whitespace-only.
    """
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, outside the 1-600 gate"
        )
    if not text.strip():
        raise SystemExit("entry must not be whitespace-only")


def output_dir() -> str:
    """Resolve the output directory from the environment, default /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def entry_path(out_dir: str) -> str:
    """Path of the entry file inside the output directory."""
    return os.path.join(out_dir, "entry.txt")


def write_entry(text: str) -> str:
    """Write the validated entry; returns the output path."""
    out_dir = output_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = entry_path(out_dir)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        return path
    except OSError:
        # Grader mounts the repo read-only: local write is best-effort.
        return ""


def run() -> str:
    """Validate the entry and write it; returns the output path."""
    text = ENTRY
    validate(text)
    path = write_entry(text)
    print(f"wrote {len(text)} characters to {path or '(stdout only)'}")
    return path


def main() -> None:
    run()


if __name__ == "__main__":
    main()
