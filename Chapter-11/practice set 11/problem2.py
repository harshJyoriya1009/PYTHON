# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):
    def bark(self):
        print("Dog is bark")

d=Dog()

d.bark()