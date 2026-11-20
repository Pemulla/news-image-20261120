#!/usr/bin/env python3
"""News image of the day (20 November 2026): copies the bundled entry.png to the output dir.

Deterministic: no network, no randomness; both runs write the same bytes.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(DST_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(DST_DIR, "entry.png"))
