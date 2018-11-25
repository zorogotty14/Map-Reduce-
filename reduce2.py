#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from operator import itemgetter
from collections import Counter
import sys
mydict={} 

for line in sys.stdin:
	   line = line.strip()
	   word, B_count = line.split('\t',) 
	   try:
		B_count = int(B_count)
	   except:
		continue
	   try:
		if word in mydict:
			mydict[word]+=B_count
			
		else:
			mydict[word]=B_count
			
	   except:
		continue
l1=(mydict.keys())
l2=(mydict.values())
l3=(counter(mydict.keys()))
print counter		
'''sorted1=sorted(zip(l1,l2),key=lambda (k,v):(v,k))
sorted1=sorted1[::1]
for i in sorted1:
	print i'''


