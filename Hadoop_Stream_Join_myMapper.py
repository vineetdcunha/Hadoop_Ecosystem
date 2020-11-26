#!/usr/bin/python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	line = line.strip()
	split = line.split('|')
	key = None
	if split[0].startswith('EMP'): #Mapper1, Employer
        	key = split[1],split[2]
		print "%s\t%s\t%s\t%s"% (key,split[1],split[2],split[3],'Employer')
	else:                                                    #Mapper2, Customer
		key = split[1],split[2]
        	print "%s\t%s\t%s\t%s"% (key,split[1],split[2],split[3],'Customer')