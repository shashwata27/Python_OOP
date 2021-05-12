class student:

    school="walter"#class variable

    def __init__(self,roll,age):
        self.rol=roll
        self.ag=age

    def get_rol(self):
        return self.rol

    def get_ag(self):#getter
        return self.ag

    def set_rol(self):#setter
        self.rol=0

    def set_ag(self):
        self.ag=5

    #def __get__(self, instance, owner):
     #   self.ag=instance
      #  student=owner

    @classmethod# using decorator
    def sch(cls):
        return cls.school#class method

    def scho(student):#class method without decorator
        return student.school

    @staticmethod#decorator
    def info():#static method can access class variables
        print("learning OOP", student.school)




c1=student("12",10)

#print(c1.__get__(c1,student))

student.info()#only way to call static method so we have to use decorator

print(c1.get_ag(),c1.get_rol(),c1.school,student.school)

c1.set_ag()

print(c1.ag)

print(c1.sch())#class method with the decorator
print(c1.scho())#class method without the decorator
print(student.sch())#without decorator this throws error


