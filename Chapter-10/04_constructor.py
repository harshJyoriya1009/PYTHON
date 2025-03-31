class Employee:
    language="Python"
    salary=15000

    def __init__(self,name,language,salary):    #dunder method which is automatically called
        self.name=name
        self.language=language
        self.salary=salary

    def info(self):
        print(f"The language of your employee is {self.language} and the salary is {self.salary}")

    @staticmethod   #Sometimes we need a function that does not use the self-parameter. We can define a static method like this: 
    def greet():
        print("Good Morning...")

harsh=Employee("Jyoriya","English",1500)
print(harsh.name,harsh.language,harsh.salary)

harsh.info()
# harsh.greet()

