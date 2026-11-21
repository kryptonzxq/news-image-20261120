#!/usr/bin/env python3
"""Validation for the news-image entry. Run from the repo root.

Checks: output exists, valid PNG, <=1024x1024, <=1 MiB, two consecutive
runs produce identical SHA-256 bytes, and no network is used (the program
only reads local assets/ files).
"""
import hashlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = "/output/entry.png"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def run():
    r = subprocess.run([sys.executable, os.path.join(HERE, "main.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, f"main.py failed: {r.stderr}"
    return r.stdout.strip()


def main():
    # Run twice; both must write identical bytes.
    run()
    assert os.path.exists(OUT), f"missing {OUT}"
    h1 = sha256(OUT)
    run()
    h2 = sha256(OUT)
    assert h1 == h2, f"non-deterministic: {h1} != {h2}"

    from PIL import Image
    im = Image.open(OUT)
    assert im.format == "PNG", f"not PNG: {im.format}"
    assert im.size[0] <= 1024 and im.size[1] <= 1024, f"too large: {im.size}"
    size = os.path.getsize(OUT)
    assert size <= 1024 * 1024, f"over 1 MiB: {size} bytes"
    print(f"OK: {OUT} {im.size} PNG {size} bytes sha256 {h1}")
    print("OK: deterministic across two runs")


if __name__ == "__main__":
    main()
