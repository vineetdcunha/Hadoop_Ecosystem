#!/usr/bin/python
import sys

curr_id = None
curr_cnt = 0
id = None
val = []
avg = 0
variance = []
# The input comes from standard input (line by line)
for line in sys.stdin:
    line = line.strip()
    # parse the line and split it by '\t'
    ln = line.split('\t')     # [1, 5]
    # grab the key
    id = ln[0]   # current received key is lo_quantity
    if curr_id == id:
        curr_cnt += 1
        val.append(int(ln[1]))
    else:
        if curr_id: # output the count, single key completed
            avg = sum(val) * 1.0 / len(val)
            variance = list(map( lambda x: (x - avg)**2, val))
            print '%s\t%f' % (curr_id, (sum(variance) * 1.0 / len(variance)) ** 0.5)
        curr_id = id
        curr_cnt = 1
        val = []
        avg = 0
        variance = []
        val.append(int(ln[1]))

# output the last key
if curr_id == id:
    avg = sum(val) * 1.0 / len(val)
    variance = list(map( lambda x: (x - avg)**2, val))
    print '%s\t%f' % (curr_id, (sum(variance) * 1.0 / len(variance)) ** 0.5) 