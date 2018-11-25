# Map-Reduce
Basic Map-reduce program to get the runs scored or wickets taken using ipl 2008 -2018 dataset.
the mapper function goes through the input file then takes batsman name column number 6, bowler name column number 8 and assigns runs column 15 and puts them in list of tuples 
reducer function reads output of mapper function and counts values and returns it.
To run the program you can use
cat input.txt | python mapper.py |python reducer.py 
