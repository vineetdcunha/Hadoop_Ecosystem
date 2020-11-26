#!/usr/bin/python
import sys

curr_id = None
id = None
valsExtendedPrice = []
# The input comes from standard input (line by line)
for line in sys.stdin:
    line = line.strip()
    # parse the line and split it by '\t'
    ln = line.split('\t')     # [1, 5]
    # grab the key
    id = ln[0]   # current received key is cnation
    if curr_id == id:
        valsExtendedPrice.append(int(ln[1]))
    else:
        if curr_id: # output the count, single key completed
            # NOTE: Change this to '%s\t%d' if your key is a string
            print '%s\t%d' % (curr_id, max(valsExtendedPrice))  # print 1\t2 if you saw two 1s
        curr_id = id   # Reset the current key to the new key (e.g., 6)
        valsExtendedPrice = []
        valsExtendedPrice.append(int(ln[1]))

# output the last key
if curr_id == id:
    print '%s\t%d' % (curr_id, max(valsExtendedPrice))
