class Employee:
    language="PY"   #This is an class attribute
    salary=1500000


harsh=Employee()
harsh.name="Harsh"
print(harsh.name,harsh.language, harsh.salary)


atif=Employee()
employeeName="Atif"  #This is an instance attribute
print(employeeName,atif.salary, atif.language)