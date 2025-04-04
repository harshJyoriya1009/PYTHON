class CEO:     #Parent class
    def __init__(self):
        print("He is CEO of Company")
    a=1

class HR(CEO):  #Child class 1
    def __init__(self):
        print("He is HR of Company")
    b=2

class Employee(HR):  #Child class 2
    def __init__(self):
        super().__init__()
        print("He is Employee of Company")
    c=3



# o=CEO()
# print(o.a)

# o=HR()
# print(o.a, o.b)

o=Employee()
print(o.a,o.b,o.c)