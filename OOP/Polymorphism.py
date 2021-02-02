class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says Woof!')


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' says Meow!')


Bobik = Dog('Bobik')
Puss = Cat('Puss')

Bobik.speak()
Puss.speak()