class Employee:     #Base class 1
    name="Harsh"
    salary=25000
    company="IT"

    def info(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class Coder:     #Base class 2
    language="Python"

    def showLanguage(self):
        print(f"The language of emplyoee is {self.language}")


class Programmer(Employee, Coder):   #Child class
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


a=Employee()
b=Programmer()

b.show()
b.showLanguage()
b.info()
