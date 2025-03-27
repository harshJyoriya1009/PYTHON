# Write a program to input eight numbers from the user and display all the unique numbers (once).


s= set()

n=int(input("Enter your number 1: "))
s.add(int(n))
n=int(input("Enter your number 2: "))
s.add(int(n))
n=int(input("Enter your number 3: "))
s.add(int(n))
n=int(input("Enter your number 4: "))
s.add(int(n))
n=int(input("Enter your number 5: "))
s.add(int(n))
n=int(input("Enter your number 6: "))
s.add(int(n))
n=int(input("Enter your number 7: "))
s.add(int(n))
n=int(input("Enter your number 8: "))
s.add(int(n))

print(s)