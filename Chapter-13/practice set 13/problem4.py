#  Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if(n%5==0):
        return True
    return False

a=[5,78,25,1,2555,968,685]

f=list(filter(divisible5,a))
print(f)