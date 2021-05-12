#we bind data and methods together within a class so change from outside cantont be done
#restrict access to methods and variables by using underscore as the prefix i.e single _ or double __
#prevents data from direct modification which is called encapsulation
class Computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000#price wouldnt change as maxprice is encapsulated by using _
c.sell()

# using setter function
c.setMaxPrice(1000)#but the class have a method within it to change that so we have to use that if we want to change
c.sell()

#eg; when two employess sub classes like sales and finance whats each others data, they cant directly acess it if the data
#is encapsulated in respective classes