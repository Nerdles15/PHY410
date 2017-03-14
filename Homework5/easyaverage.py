#easier way to do P2, running out of time

import sys

score = sys.argv[1]

def calculate_average(grade):
	file = open(grade)
	totscore = 0.0
	numstudents = 0
	for line in file:
		print (line)
		info = line.split(',')
		score = float(info[2])
		numstudents += 1
		totscore += score
	return totscore/numstudents

print("\nOverall average is: " + str(calculate_average(score)))