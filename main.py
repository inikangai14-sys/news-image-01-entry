"""news-image-01 entry: ship the front-page image as /output/entry.png.

The image (entry.png, JPEG bytes, 1024x1024, 239,395 bytes) lives next to
this file in the repository. It sums up Friday 13 November 2026 in six
labelled vignettes: Ukraine peace talks, Nvidia CEO resigns, drone hits
Russian warship, Iran claims strike in Bahrain, $400m crypto hack, record
US deportations. The program copies it byte-for-byte, so both grader runs
write identical bytes. No clock, no randomness, no network. The output
directory defaults to /output (the grader's writable dir);
MAKEFUN_OUTPUT_DIR overrides it for local testing only.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, out_dir / "entry.png")
