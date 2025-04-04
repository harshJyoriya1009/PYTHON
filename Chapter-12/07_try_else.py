try:
    a=int(input("Enter your number:"))
    print (a)

except Exception as e:
    print(e)

else:
    print("Hello world")       # This is executed only if the try was successful 