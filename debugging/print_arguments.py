#!/usr/bin/python3
import sys

for i in range(1, len(sys.argv)):  # Changed from range(len(sys.argv)) to range(1, len(sys.argv))
    print(sys.argv[i])