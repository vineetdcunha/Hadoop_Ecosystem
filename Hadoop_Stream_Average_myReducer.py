#!/usr/bin/python
import sys

curr_id = None
curr_cnt = 0
id = None
val = 0
# The input comes from standard input (line by line)
for line in sys.stdin:
    line = line.strip()
    # parse the line and split it by '\t'
    ln = line.split('\t')     # [1, 5]
    # grab the key
    id = int(ln[0])   # current received key is lo_quantity
    if curr_id == id:
        curr_cnt += 1
        val = val + int(ln[1])
    else:
        if curr_id: # output the count, single key completed
            # NOTE: Change this to '%s\t%d' if your key is a string
            print '%d\t%d' % (curr_id, (val/curr_cnt))  # print 1\t2 if you saw two 1s
        curr_id = id   # Reset the current key to the new key (e.g., 6)
        curr_cnt = 1
        val = 0
        val = val + int(ln[1])

# output the last key
if curr_id == id:
    print '%d\t%d' % (curr_id, (val/curr_cnt))
