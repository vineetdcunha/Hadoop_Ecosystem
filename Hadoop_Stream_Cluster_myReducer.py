#!/usr/bin/python
import sys

curr_id = None
curr_cnt = 0
id = None
val1 = 0
val2 = 0
val3 = 0
val4 = 0
val5 = 0
val6 = 0
val7 = 0
val8 = 0
val9 = 0
val10 = 0
# The input comes from standard input (line by line)
for line in sys.stdin:
    line = line.strip()
    # parse the line and split it by '\t'
    ln = line.split('\t')     # [1, 5]
    # grab the key
    id = int(ln[0])   # current received key is lo_quantity
    if curr_id == id:
        curr_cnt += 1
        val1 = val1 + float(ln[1])
        val2 = val2 + float(ln[2])
        val3 = val3 + float(ln[3])
        val4 = val4 + float(ln[4])
        val5 = val5 + float(ln[5])
        val6 = val6 + float(ln[6])
        val7 = val7 + float(ln[7])
        val8 = val8 + float(ln[8])
        val9 = val9 + float(ln[9])
        val10 = val10 + float(ln[10])
    else:
        if curr_id: # output the count, single key completed
            # NOTE: Change this to '%s\t%d' if your key is a string
            print '%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f' % (curr_id, (val1/curr_cnt), (val2/curr_cnt), (val3/curr_cnt), (val4/curr_cnt), (val5/curr_cnt), (val6/curr_cnt), (val7/curr_cnt), (val8/curr_cnt), (val9/curr_cnt), (val10/curr_cnt))  # print 1\t2 if you saw two 1s
        curr_id = id   # Reset the current key to the new key (e.g., 6)
        curr_cnt = 1
        val1 = 0
        val2 = 0
        val3 = 0
        val4 = 0
        val5 = 0
        val6 = 0
        val7 = 0
        val8 = 0
        val9 = 0
        val10 = 0
        val1 = val1 + float(ln[1])
        val2 = val2 + float(ln[2])
        val3 = val3 + float(ln[3])
        val4 = val4 + float(ln[4])
        val5 = val5 + float(ln[5])
        val6 = val6 + float(ln[6])
        val7 = val7 + float(ln[7])
        val8 = val8 + float(ln[8])
        val9 = val9 + float(ln[9])
        val10 = val10 + float(ln[10])

# output the last key
if curr_id == id:
    print '%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f' % (curr_id, (val1/curr_cnt), (val2/curr_cnt), (val3/curr_cnt), (val4/curr_cnt), (val5/curr_cnt), (val6/curr_cnt), (val7/curr_cnt), (val8/curr_cnt), (val9/curr_cnt), (val10/curr_cnt))
