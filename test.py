x=10
def lop():
    x=5
    print(x)
def lop1():
    global x
    x=6
    # for y in range(x):
    #     print(y+2)
    #     x-=1
    print(x)

lop()
print(x)
lop1()
print(x)