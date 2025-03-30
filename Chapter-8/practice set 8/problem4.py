# Write a recursive function to calculate the sum of first n natural numbers. 

a=int(input("Enter the number how many sum you have to do: "))

def sumNum(a):
    if(a==0):
        return 0
    elif(a==1):
        return 1
    else:
        return a + sumNum(a-1)
    
print(f"The sum of your number is: {sumNum(a)}")