# OOP in Python

# --------------------------------- STUDENT ------------------------------------
class Student:
	def __init__(self,name,age,grade):
		self.name = name 
		self.age = age
		self.grade = grade

	def get_grade(self):
		return self.grade

# ---------------------------------- COURSE -----------------------------------
class Course:
	def __init__(self,name,max_students):
		self.name = name
		self.max_students = max_students
		self.students = []
		
	def add_student(self,student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		grades = 0
		for student in self.students:
			grades += student.get_grade()

		return grades/len(self.students)


s1 = Student("Aktan",21,97)
s2 = Student("Alikhan",21,91)
s3 = Student('Ulan',20,85)

course = Course("Algebra",5)
course.add_student(s1)
course.add_student(s3)
course.add_student(s2)
print(course.get_average_grade())