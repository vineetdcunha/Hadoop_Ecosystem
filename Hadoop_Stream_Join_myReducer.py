#!/usr/bin/python

import sys
import itertools

currentKey = None
valsEmployer = []
valsCustomer = []
employervalue = None
customervalue = None
phonevalue = None
addressvalue = None
fname = None
lname = None

# input comes from STDIN
for line in sys.stdin:

	split = line.strip().split('\t')    # 'Q11 \t Val1 \t Val2 \t Val3'
	key = split[0]
	line_value = '\t'.join(split[1:])

	if currentKey == key:  # Same key
		if line_value.endswith('Employer'):
            		employervalue = line_value.strip().split('\t')
			fname = employervalue[0]
			lname = employervalue[1]
			phonevalue = employervalue[2]
			valsEmployer.append([fname, lname, phonevalue])
		if line_value.endswith('Customer'):
			customervalue = line_value.strip().split('\t')
			addressvalue = customervalue[2]
			valsCustomer.append(addressvalue)
	else:
		if currentKey:
			lenEmployer = len(valsEmployer)
			lenCustomer = len(valsCustomer)
			if (lenEmployer*lenCustomer > 0):
				for i in valsEmployer:
					for j in valsCustomer:
						print '%s\t%s' %('\t'.join(i),j)
		currentKey = key
		valsEmployer = []
		valsCustomer = []
		fname = None
		lname  = None
		phonevalue = None
		addressvalue = None
		if line_value.endswith('Employer'):
            		employervalue = line_value.strip().split('\t')
			fname = employervalue[0]
			lname = employervalue[1]
			phonevalue = employervalue[2]
			valsEmployer.append([fname, lname, phonevalue])
		elif line_value.endswith('Customer'):
            		customervalue = line_value.strip().split('\t')
			addressvalue = customervalue[2]
			valsCustomer.append(addressvalue)
lenEmployer = len(valsEmployer)
lenCustomer = len(valsCustomer)
if (lenEmployer*lenCustomer > 0):
	for i in valsEmployer:
		for j in valsCustomer:
			print '%s\t%s' %('\t'.join(i),j)