class Employee:
    language="Python"
    salary=15000

    def info(self):
        print(f"The language of your employee is {self.language} and the salary is {self.salary}")

    @staticmethod   #Sometimes we need a function that does not use the self-parameter. We can define a static method like this: 
    def greet():
        print("Good Morning...")

harsh=Employee()

harsh.info()
harsh.greet()

# We used "self" to pass arguments..