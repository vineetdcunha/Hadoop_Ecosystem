#!/usr/bin/python

import sys

for line in sys.stdin:
        line = line.strip()
        vals = line.split("\t")
        print "%s\t%d" % (vals[0], int(vals[1]))  # 123 456
