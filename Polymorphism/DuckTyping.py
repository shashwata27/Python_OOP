class Pycharm:
    def execute(self):
        print("processing")
class MyPythonEditor:
    def execute(self):
        print("spell check")
        print("covention check")
        print("processing")

class Editor:

    def Run(self,IDE):
        print("starting")
        IDE.execute()#this is duck typing where we name all the methods in previous classes as same as this

ID1=Pycharm()# we can change the ID1 object type to differnt class and make it execute() behave different

Edtr=Editor()
Edtr.Run(ID1)#ID1 is of type Pycharm


print()
ID2=MyPythonEditor()

Edtr=Editor()
Edtr.Run(ID2)#ID2 is of type MyPythonEditor