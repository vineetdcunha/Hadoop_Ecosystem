#!/usr/bin/python
import sys

for line in sys.stdin:
	line = line.strip().split('\t')
	week = line[7]
	month = line[8]
	year = line[9]
	val2 = ''.join([week,month,year])
	line[7] = val2
	print '\t'.join([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[10],line[11],line[12]])
