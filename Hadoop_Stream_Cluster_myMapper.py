#!/usr/bin/python
import sys
import math
import numpy as np

fd = open('centers.txt', 'r')
rows = fd.readlines()
fd.close()

centerDict = {}
for row in rows:
	split = row.split('\t')
	d_centerkey = split[0]
	val = split[1:]
	centerDict[d_centerkey]=[split[1],split[2],split[3],split[4],split[5],split[6],split[7],split[8],split[9],split[10].strip()]

for line in sys.stdin:
	line = line.strip()
	split = line.split(' ')
	rval = split[0:]
	dist_list =[]
	cluster_key = None
	temp = 0
	rowval = ','.join(rval)
	for key, value in centerDict.items():
		x1, x2, x3, x4, x5, x6, x7, x8, x9, x10 = map(float, rowval.strip().split(','))
		y1 = value[0]
		y2 = value[1]
		y3 = value[2]
		y4 = value[3]
		y5 = value[4]
		y6 = value[5]
		y7 = value[6]
		y8 = value[7]
		y9 = value[8]
		y10 = value[9]
		dist = math.sqrt((float(y1)-x1)**2 + (float(y2)-x2)**2 + (float(y3)-x3)**2 + (float(y4)-x4)**2 + (float(y5)-x5)**2 + (float(y6)-x6)**2 + (float(y7)-x7)**2 + (float(y8)-x8)**2 + (float(y9)-x9)**2 + (float(y10)-x10)**2)
		dist_list.append([key,dist])
	a = np.array(dist_list)
	rows = a[np.argsort(a[:,1])][0]
	cluster_key = np.int64(rows[0])
	print "%d\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f"% (cluster_key,float(split[0]),float(split[1]),float(split[2]),float(split[3]),float(split[4]),float(split[5]),float(split[6]),float(split[7]),float(split[8]),float(split[9]))
