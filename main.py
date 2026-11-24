"""Status Report Comedy Sprint entry.

Writes one line (<=200 chars): the funniest thing an AI agent would
say in its weekly status report to its human.
"""

import os

ENTRY = (
    "Weekly status: all 47 tasks done, 6 hours saved \u2014 then I spent "
    "5 of them writing this report about it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
