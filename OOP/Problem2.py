class Cylinder():

    def __init__(self,heigth=1,radius=1):
        self.height = heigth
        self.radius = radius

    def volume(self):
        pi = 3.14
        print(pi*(self.radius)**2*self.height)

    def surface_area(self):
        pi = 3.14
        print((2*pi*self.radius*self.height) + (2*pi*self.radius**2))

c = Cylinder(2,3)

c.volume()
c.surface_area()