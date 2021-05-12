#abstraction provides common structure for different classes and binds different classes
#abstrat classes are use to make some restriction on the child/sub class, so that they have some sort of signature from
#parent and also to protect data

from  abc import ABC,abstractmethod
#we can't make instances of abstract class and
# python dosen't have built-in concept of abstraction so we use ABC from abc
class shape(ABC):#abstract class
    def print(self):#normal method
        print("normal method within abstarct class")

    @abstractmethod
    def calculateArea(self):#abstract method: this have only declareation but no defination/body
        pass

class rectangle(shape):#implementations are to be defined in the child of the abstarct class
    #all the abstract methods are to defined here, if we miss it throws error
    def __init__(self):
        self.name="rectangle"
        self.length=5
        self.width=6
    def calculateArea(self):#we must define the method here if we want to instantiate this class,
        # else this is a abstract method too

        area=self.length*self.width#defining implementation
        print(area)

rec=rectangle()
rec.calculateArea()

#eg; a company wants to have only graduate employes so it creates a graduate emp abstarct class and all the other class of
#differnt kind of employes inherit this abstract class