class Robot:
    def __init__(self,givenColour,givenName,givenWeight):#init gets called when ever a object is created
        self.name=givenName#self stands for the object at that moment, and we assign the paased value in the object creation.. .
        self.colour=givenColour#to that attributes of the object
        self.weight=givenWeight

    def output(self):
        print(self.name+','+self.colour+','+str(self.weight)+"lbs")#we have to use self here because name or givenname isnt a local...
        #local variable it belongs to the object at that moment, and self represets the object

r1=Robot('Blue','Robo',87)
r2=Robot('Red','Momo',67)

#constructor __init__ is responsible for allocating the spaces for variables
#each time we execute the code different objects are created in the heap memory, so they will have different address
print(id(r1),id(r2))

r1.output()
print(r2.colour)
