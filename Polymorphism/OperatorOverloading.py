#the operators i.e. +, -, * behave differently with different type of inputs
#when we pass + to two stings it calls str.__add__()
# but when we pass two intergers in + operator int.__add__() gets called
# this means the operator + is overloaded for different parameters just like method OverLoading

class Student:
    def __init__(self,marks1,marks2):
        self.m1=marks1
        self.m2=marks2
    def __add__(self, other):#overloading predefined add function for out Student class
        m1=self.m1+other.m1
        m2=self.m2+other.m2

        return Student(m1,m2)# returns the class with added numbers of students
    def __gt__(self,other):
        s1total=self.m1+self.m2
        s2total=other.m1+other.m2

        if s1total>s2total:
            return True
        else:
            return False
    def __str__(self):#print function calls str() by default
        return "marks of the student are "+str(self.m1)+" "+str(self.m2)





s1=Student(30,40)
s2=Student(70,80)


s3= s1+s2# ' + ' operator works directly on instances of Student class as we Overloaded add() for Student class
print(s3.m1,s3.m2)


verdict=s1>s2# ' > ' operator works directly on instances of Student class as we Overloaded gt() i.e. greater than for Student class
if verdict==True:
    print("student 1 scores more")
else:
    print("student 2 scores more")


print(s3)#calls the Str() method by default which is over loaded to show marks of students


a=6#since a is interger we can acess int bulit-in methods by a and here 'a' is passed to the self of  add() method
print(a.__add__(5))
print(int.__add__(6,5))#here we call the method by class name so, we cant pass variable through self,both values go to *args



