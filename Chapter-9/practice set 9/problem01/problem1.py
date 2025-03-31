# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘Twinkle’. 

f = open("poems.txt")
c = f.read()
if("Twinkle" in c):
    print("Yes, the word Twinkle is present in that file")
else:
    print("No, the word Twinkle is not present in that file")
f.close()