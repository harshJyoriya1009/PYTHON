# Write a program to find out whether a given post is talking about “Harry” or not. 


post=input("Enter your post: ")

if("Harry".lower() in post.lower()):
    print("Given post is talking about “Harry”")

else:
    print("Given post is not talking about “Harry”")