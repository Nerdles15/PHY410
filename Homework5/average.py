#Create a program to input records from a text file
#and calculate the average of the students' grades, redo HW4P1


import sys
from StudentRecord import StudentRecord

val = sys.argv[1]

def main():

	file = open(val)
	scores = []
	numstudents = 0
	totscore = 0.0
	for info in file:
		student = StudentRecord()
		student.input(info)
		scores.append(student)
		numstudents += 1
		totscore += student.score()

	average = totscore/numstudents
	print ("Overall average: " + average + ".")

#if __name__ == "__main__":
#	main()