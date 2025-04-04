a=int(input("Enter number a: "))
b=int(input("Enter number b: "))

if(b==0):
    raise ZeroDivisionError("Hey we can't divide any number with zero")   # It will crash your program 
else:
    print(f"The answer of a/b is {a/b}")

print("HELLO")