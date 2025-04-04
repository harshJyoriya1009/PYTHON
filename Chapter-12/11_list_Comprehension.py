myList=[1,8,7,3,4]

# squareList=[]

# for item in myList:
#     squareList.append(item*item)

# print(myList)
# print(squareList)


#This can be simplified using Comprehension function
squareList=[item*item for item in myList ]
print(myList)
print(squareList)

