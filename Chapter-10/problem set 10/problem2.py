# Write a class “Calculator” capable of finding square, cube and square root of a number. 

class Calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"The square of your number {self.n}: {self.n*self.n}")
    
    def cube(self):
        print(f"The square of your number {self.n}: {self.n*self.n*self.n}")
    
    def squareRoot(self):
        print(f"The square of your number {self.n}: {self.n*1/2}")

a=Calculator(4)
a.square()
a.cube()
a.squareRoot()
        