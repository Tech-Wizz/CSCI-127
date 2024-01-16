class Area:

    def __init__(self,name,legth,width):
        self.legth = legth
        self.width = width
        self.name = name.capitalize

    def __str__(self):
        answer = self.name + "has area" + int(self.legth*self.legth)
        return answer

    def Rectangle(N,L,W):
        Area(N,L,W)

    def Square(N,L):
        Area(N,L,L)

r1 = Rectangle("Rectangle 1",5,6)
print(r1)
s1 = Square("Square 1",7)
print(s1)
