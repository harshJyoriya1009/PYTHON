# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 


class Demo:
    a=4

obj=Demo()
print(obj.a)

obj.a=0
print(obj.a)

print(Demo.a)

#So the answer is no..it means class attribuit doesn't change but instance attribute add..