#!/usr/bin/env python
import sys

def read_input(file):
    for line in file:
        yield line.split('\t')

def main(separator='\t'):
    i = 1
    data = read_input(sys.stdin)
    for words in data:
	if(len(words) == 21 and words[19]!="run out" and words[19]!= "retired hurt"):
		if(i==1):
			i+=1
			continue
		if(words[18] != ""):
			key=(words[8],words[18])
			print '%s\t%d' % (key,1)


if __name__ == "__main__":
    main()



