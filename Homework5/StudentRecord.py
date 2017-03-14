#Create a program to input records from a text file
#and calculate the average of the students' grades, redo HW4P1


class StudentRecord():
	"""holds student information"""

	def __init__(self, lname, fname, score):
		"""attributes of each student's info"""
		self.lname = lname
		self.fname = fname
		self.score = float(score)

	def __str__(self):
		return self.lname + ', ' + self.fname + ', ' + self.score

	def input(self, line):
		"""input lines from file"""
		self.lname, self.fname = [s.strip() for s in line.split(",")]
		self.score = float(score)