#!/usr/bin/python
import sys

for line in sys.stdin:
	line = line.strip().split('\t')
	val1 = line[6].split(' ')
	Word1 = val1[0]
	Word2 = val1[1]
	Word3 = val1[2]
	val2 = '~'.join([Word3,Word2,Word1])
	line[6] = val2
	print '\t'.join([line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8]])
