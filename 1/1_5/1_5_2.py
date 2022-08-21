class Point:
    def __init__(self,x=0,y=0,color="black"):
        self.x=x
        self.y=y
        self.color=color


p1 = Point(10, 20)
p2 = Point(12, 5, 'red')

points=[]
for i in range(1, 2000, 2):
    if i==3:
        points.append(Point(i,i,'yellow'))
    else:
        points.append(Point(i,i))