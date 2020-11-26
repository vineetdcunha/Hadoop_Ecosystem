#!/usr/bin/python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	split = line.split('|')
	if split[1].startswith('Customer'): #Mapper1, Customer
		if split[5] == 'AFRICA':
			print "%d\t%s\t%s"% (int(split[0]),split[4],'Customer')
	else:                                                    #Mapper2, lineorder
		if split[11] == '6':
        		print "%s\t%s\t%s"% (int(split[2]),split[9],'Lineorder')