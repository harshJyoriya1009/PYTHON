# Write a program to find the maximum of the numbers in a list using the reduce function. 

from functools import reduce

l=[5,78,25,1,2555,968,685]
def greater5(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater5,l))