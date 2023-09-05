class Point:
    def __init__(self,x,y):
        self.x=x  #self==this keyword, refer current object
        self.y=y #initialize x and y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

point=Point(10,20)
point.x=11
print(point.x)