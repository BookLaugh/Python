class Pet:
	def __init__(self,name,age):
		self.name = name
		self.age = age
	
	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("I do not know what to say")


class Dog(Pet):

	def __init__(self,name,age,color):
		Pet.__init__(self,name,age)
		self.color = color

	def speak(self):
		print("Bark")

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old I am {self.color}")



class Cat(Pet):
	def speak(self):
		print("Meow")


class Fish(Pet):
	pass

p = Pet("Jimmy",19)
p.speak()
c = Cat('Johny',8)
c.speak()
d = Dog("Sweety",4,"Blue")
d.show() 
f = Fish("Dori",5)
f.speak()