#!/usr/bin/python

import sys
import itertools

currentKey = None
valsLineorder = []
valsCustomer = []
lineordervalue = None
customervalue = None
cnation = None
extendedprice = None

# input comes from STDIN
for line in sys.stdin:

	split = line.strip().split('\t')    # 'Q11 \t Val1 \t Val2 \t Val3'
	key = split[0]
	line_value = '\t'.join(split[1:])

	if currentKey == key:  # Same key
		if line_value.endswith('Customer'):
            		customervalue = line_value.strip().split('\t')
			cnation = customervalue[0]
			valsCustomer.append(cnation)
		if line_value.endswith('Lineorder'):
			lineordervalue = line_value.strip().split('\t')
			extendedprice = lineordervalue[0]
			valsLineorder.append(extendedprice)
	else:
		if currentKey:
			lenLineorder = len(valsLineorder)
			lenCustomer = len(valsCustomer)
			if (lenLineorder*lenCustomer > 0):
				for i in valsCustomer:
					for j in valsLineorder:
						print '%s\t%s' %(i,j)
		currentKey = key
		valsLineorder = []
		valsCustomer = []
		cnation = None
		extendedprice = None
		if line_value.endswith('Customer'):
            		customervalue = line_value.strip().split('\t')
			cnation = customervalue[0]
			valsCustomer.append(cnation)
		elif line_value.endswith('Lineorder'):
            		lineordervalue = line_value.strip().split('\t')
			extendedprice = lineordervalue[0]
			valsLineorder.append(extendedprice)
lenLineorder = len(valsLineorder)
lenCustomer = len(valsCustomer)
if (lenLineorder*lenCustomer > 0):
	for i in valsCustomer:
		for j in valsLineorder:
			print '%s\t%s' %(i,j)