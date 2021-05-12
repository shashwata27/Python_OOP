class student:
    def __init__(self,roll,name,rand,am,torage):
        self.rol=roll
        self.nam=name
        self.laptp=self.laptop(rand,am,torage) #object of inner class inside the outer class

    def show(self):
        print(self.rol,self.nam)
        self.laptp.show()

    class laptop:
        def __init__(self,brand,ram,storage):
            self.brnd=brand
            self.rm=ram
            self.strge=storage
        def show(self):
            print(self.brnd,self.rm,self.strge)

s1=student(23,"Shashwata Saha","acer",16,2000)

s1.show()#calling the show of the outer class, both show methods are different

lap1=s1.laptp# acessing the inner show method using the exsisting object, we had to use the object created inside the outer class
lap1.show()# laptp is object of inner class but attribute of outer


#lap1=s1.laptop("acer",16,2000)

#lap2=student.laptop("HP",8,1000)#creating object of inner class outside the class