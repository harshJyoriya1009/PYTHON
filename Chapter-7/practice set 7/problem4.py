#  Write a program to find whether a given number is prime or not. 

n=int(input("Enter your number: "))

for i in range(2,n):
    if(n%i==0):
        print("Given number is not prime")
        break
    else:
        print("Given number is prime")
        break