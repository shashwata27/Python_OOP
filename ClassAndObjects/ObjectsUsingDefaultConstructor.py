class Robot:
    def output(self):
        print("my name is "+self.name)


r1=Robot()#creating an object of class Robot
r1.name='robo'#setting attribute name to some value for object r1
r1.output()#calling method of class Robot for object r1

r2=Robot()
r2.name="momo"
r2.output()

r3=Robot()
r3.nam="jojo"
print(r3.nam)#nam attribute gets defined but it's not the correct atribute we wanted to define
r3.output()
