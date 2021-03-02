class Person:
	number_of_people = 0
	Gravity = -9.8

	def __init__(self,name):
		self.name = name
		Person.add_person()
	@classmethod
	def number_of_people_(cls):
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people+=1



p1 = Person("Huskie")
p2 = Person("Dazzle")
p3 = Person("Delta")
print(Person.number_of_people_())