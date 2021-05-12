class car:
    wheels=4#class variable
    def __init__(self,clr):
        self.colour=clr#colour is instance variable

c1=car("yellow")
print(c1.colour,c1.wheels)

print(car.wheels)#we can also call it by the class
