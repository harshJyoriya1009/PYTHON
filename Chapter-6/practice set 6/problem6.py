# Write a program to calculate the grade of a student from his marks from the following scheme: 
#                  90 – 100 => Ex 
#                  80 – 90 => A 
#                  70 – 80 => B 
#                  60 – 70  =>C 
#                  50 – 60 => D 
#                  <50  => F 

student_grade=int(input("Enter your grade: "))

if(student_grade<=100 and student_grade>=90):
    print("Excellent")

elif(student_grade<90 and student_grade>=80):
    print("A")

elif(student_grade<80 and student_grade>=70):
    print("B")

elif(student_grade<70 and student_grade>=60):
    print("C")

elif(student_grade<60 and student_grade>=50):
    print("D")

elif(student_grade<50):
    print("F")