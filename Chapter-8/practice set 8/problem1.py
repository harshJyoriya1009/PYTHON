#  Write a program using functions to find greatest of three numbers. 

# def greatestNum(a,b,c):
#     if(a>b and a>c):
#         print("a is greatest")
#     elif(b>a and b>c ):
#         print("b is greatest")
#     else:
#         print("c is greatest")


# greatestNum(10,8,7)


a=int(input("Enter number a: "))
b=int(input("Enter number b: "))
c=int(input("Enter number c: "))

# def greatestNum(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
# print(f"The greatest number is {greatestNum(a,b,c)} ")



def greatestNum(a,b,c):
    if(a>b and a>c):
        print(f"Gretest number is {a}")
    elif(b>a and b>c):
        print(f"Gretest number is {b}")
    else:
        print(f"Gretest number is {c}")
# print(f"The greatest number is {greatestNum(a,b,c)} ")
greatestNum(a,b,c)
        