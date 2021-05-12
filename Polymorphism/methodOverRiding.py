class A:
    def show(self,cls="A"):
        print("show of class "+ cls)

class B(A):#this simply replaces the show method of A
    def show(self, cls="B"):
        print("show of class " + cls)

class C(A):
    pass

b=B()
b.show()

c=C()
c.show()#uses show of Class A as it isnt overRiding



#PREFERABLE to work by extending the function defenation
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)#extending the defination than simply replacing it

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

t=Triangle()

t.inputSides()
t.dispSides()
t.findArea()