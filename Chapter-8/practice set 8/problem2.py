# Write a python program using function to convert Celsius to Fahrenheit.

a=int(input("Enter your temperature: "))

def converter(a):
    temp= (a*(9/5))+32
    return temp

print(f"Here is your temperature in fahrenheit: {converter(a)}")