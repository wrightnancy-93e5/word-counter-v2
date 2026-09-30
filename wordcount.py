#!/usr/bin/env python3
"""Word/char counter + top kata dari file teks."""
import sys
from collections import Counter
text = open(sys.argv[1], encoding="utf-8").read()
words = text.split()
top = Counter(w.strip(".,!?\"'").lower() for w in words if len(w) > 3).most_common(10)
print(f"chars={len(text)} words={len(words)}")
print("top kata:", top)
