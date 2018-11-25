#!/usr/bin/env python


from itertools import groupby
from operator import itemgetter

import sys
mydict={} 

for line in sys.stdin: #reads inout from kernel line by line 
 	   line = line.strip()
	   word, W_count = line.split('\t',1) #splits every word in a line using tab width as separator and assigns 1 to word
	   try:
		W_count = int(W_count)
	   except:
		continue
	   try:
		if word in mydict:
			mydict[word]+=1 #if the word is present in dictionary then increment the value 
		else:
			mydict[word]=1 #if the word doesnt exist in dictionary then assign 1 
	   except:
		continue
l1=(mydict.keys())
l2=(mydict.values())
sorted1=sorted(zip(l1,l2),key=lambda (k,v):(v,k)) # sorts the two list accoring to value in desecending order
sorted1=sorted1[::-1]
for i in sorted1:
	print i


