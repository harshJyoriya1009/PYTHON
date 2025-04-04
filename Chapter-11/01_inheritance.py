class Employee:     #Base class
    name="Harsh"
    salary=25000
    company="IT"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

# class  Programmer:
#      name="Harsh"
#      salary=25000
   
#      def show(self):
#         print(f"The name is the {self.name} and the salary is {self.salary}")
#      def language(self):
#         print(f"The labguage of emplyee is {self.language}")

class Programmer(Employee):   #Child class
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


a=Employee()
b=Programmer()

a.show()
b.show()

print(a.company, b.company)
