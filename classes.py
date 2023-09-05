class point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1= point() #objeect created
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2= point()
point2.x=25
print(point2.x)