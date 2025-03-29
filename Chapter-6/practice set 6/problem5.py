# Write a program which finds out whether a given name is present in a list or not. 

list=["Harsh", "Atif", "Purohit", "Sachin", "Dev", "Rahul"]

name=input("Enter your name: ")

if(name in list):
    print(f"{name} is in the list")

else:
    print(f"{name} your name is not in the list ")