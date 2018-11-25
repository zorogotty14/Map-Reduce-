#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

from itertools import groupby
from operator import itemgetter

import sys
mydict={} 

for line in sys.stdin:
	   line = line.strip()
	   word, W_count = line.split('\t',1) 
	   try:
		W_count = int(W_count)
	   except:
		continue
	   try:
		if word in mydict:
			mydict[word]+=1
		else:
			mydict[word]=1
	   except:
		continue
l1=(mydict.keys())
l2=(mydict.values())
sorted1=sorted(zip(l1,l2),key=lambda (k,v):(v,k))
sorted1=sorted1[::-1]
for i in sorted1:
	print i


