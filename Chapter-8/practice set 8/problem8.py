# Write a python function to print multiplication table of a given number.


n=int(input("Enter your number: "))


def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

table(n)