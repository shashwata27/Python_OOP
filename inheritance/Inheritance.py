class A:#superClass/SubClass
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class Wild:
    def featureWild(self):
        print("Feature Wild is working")


class B(A):#B is child class of A i.e. B can access features of A
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(B):#multilevel inheritance, inherits from both A and B
    def feature5(self):
        print("Feature 5 working")

    def feature6(self):
        print("Feature 6 working")

class D(A,Wild):#multiple inheritance, cant inherit multiplying from A and B(no MRO) as A is alredy super class of B
    def feature7(self):
        print("Feature 7 working")

    def feature8(self):
        print("Feature 8 working")



a1=A()
b1=B()
c1=C()
d1=D()


print(a1.feature1(),a1.feature2())
print(b1.feature1(),b1.feature4())#b1 can access both class A and B but a1 cant access both
print(c1.feature1(),c1.feature3(),c1.feature5())#having features of both A and B
print(d1.feature1(),d1.feature2(),d1.featureWild())


