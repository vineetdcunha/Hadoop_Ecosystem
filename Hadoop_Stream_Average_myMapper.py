#!/usr/bin/python

import sys

for line in sys.stdin:
        line = line.strip()
        vals = line.split("|")
        if int(vals[11]) >= 6 and int(vals[11]) <=8:
                print "%d\t%d" % (int(vals[8]), int(vals[12]))  # 123 456
