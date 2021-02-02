import math
class Line():

    def __init__(self,coor1,coor2):

        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        print(math.sqrt((x2-x1)**2 + (y2-y1)**2)) 

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        print((y2-y1) / (x2-x1))


coordinator1 = (3,2)
coordinator2 = (8,10)
li = Line(coordinator1,coordinator2)

li.distance()
li.slope()





