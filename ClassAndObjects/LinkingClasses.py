class Robot:
    def __init__(self,n,c,w):
        self.name=n
        self.colour=c
        self.weight=w
    def intro(self):
        print("my name is "+self.name+" colour is "+self.colour+" and I weight"+str(self.weight)+"lbs.")

r1=Robot("momo","Green",78)
r2=Robot("jojo","yellow",98)

class Person:
    def __init__(self,n,p,i):
        self.name=n
        self.personality=p
        self.Is_sitting=i
    def standup(self):
        self.Is_sitting=True
    def sitdown(self):
        self.Is_sitting=False

p1=Person("sam","bright",True)
p2=Person("joe","dull",False)

p1.OwnsRobot=r2
p2.OwnsRobot=r1#interconnecting classes.Here p2 owns robot r1

r1.intro()
p2.OwnsRobot.intro()#both calls the same method, as Ownsrobot attribute of Person have Robot class inside it
print("p1 owns robot "+p1.OwnsRobot.name)