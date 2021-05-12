class A:#superClass/SubClass
    def __init__(self):
        print("init of A")

    def feature1(self):
        print("Feature 1-A working")

    def feature2(self):
        print("Feature 2 working")

class Wild:
    def __init__(self):
        print("init of wild")

    def feature1(self):
        print("Feature 1-wild working")

    def featureWild(self):
        print("Feature Wild is working")

class B(A):#B is child class of A i.e. B can access features of A
    def __init__(self):
        super().__init__()#if we want to call the constructor of it super class too
        print("init of B")#by default it will call its own init

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")

class D(A,Wild):
    def __init__(self):
        print("init of D")
        super().__init__()#prefers the left most class's constructor by MRO i.e. A here
    def feature7(self):
        print("Feature 7 working")

    def feature8(self):
        print("Feature 8 working")

    def feature9(self):
        super().featureWild()

a1=A()
print()
b1=B()
print()
d1=D()
d1.feature1()#same thing with the methods it prefers the left one, not calling feature1() from class wild
d1.feature9()#used super to access the FeatureWild from WILD class