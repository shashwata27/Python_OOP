#BETTER PRACTICE: overloading using *args
class Stuident:
    def sum(self,*args):
        s=0
        for x in args:
            s+=x
        return s

s2=Stuident()

print(s2.sum(3,2,4,1,4))

# class boy(Stuident):
#     def sum(self,a,b):
#         pass



#Overloading using None
class Student:
    #def __init__(self,marks1,marks2):
        #self.m1=marks1
        #self.m2=marks2

    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif b!=None and c==None:
            s=a+b
        else:
            s=a
        #print(s)
        return s

s1=Student()

print(s1.sum(2,3))