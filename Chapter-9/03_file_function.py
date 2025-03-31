f=open("file.txt")

# for print all lines
lines=f.readlines()
print(lines)

# for print single lines
line1=f.readline()
print(line1, type(line1))

line2=f.readline()
print(line1, type(line2))

line3=f.readline()
print(line1, type(line3))

f.close()