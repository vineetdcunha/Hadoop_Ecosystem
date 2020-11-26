#!/usr/bin/python

import sys

for line in sys.stdin:
        line = line.strip()
        vals = line.split("|")
        if int(vals[8]) >= 15 and int(vals[8]) <=18:
                print "%s\t%d" % (vals[16], int(vals[14]))  # 123 456
