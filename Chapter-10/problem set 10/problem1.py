# Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class Programmer:
    company="Microsoft"

    def __init__(self,name,salary,year):
        self.name=name
        self.salary=salary
        self.year=year


p=Programmer("Jyoriya",150000000,2025)
print(p.name,p.salary,p.year,p.company)
        
r=Programmer("rahul",15000,2023)
print(r.name,r.salary,r.year,r.company)
        