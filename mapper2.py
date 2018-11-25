#!/usr/bin/env python
import sys

def read_input(file):
    for line in file:
        yield line.split('\t')

def main(separator='\t'):
    i = 1
    data = read_input(sys.stdin)
    for words in data:
	if(len(words) == 21):
		if(i==1):
			i+=1
			continue
		if(words[15] != "" and words[15] != "0"):
			key=(words[6],words[8])
			print '%s\t%s' % (key,words[15])


if __name__ == "__main__":
    main()



