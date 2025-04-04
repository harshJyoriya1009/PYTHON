class CEO:     #Parent class
    a=1

class HR(CEO):  #Child class 1
    b=2

class Employee(HR):  #Child class 2
    c=3

o=CEO()
print(o.a)

o=HR()
print(o.a, o.b)

o=Employee()
print(o.a,o.b,o.c)