# Write a class "Calculator" capable of finding square,cube and square root of a number.
class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
         print(f"Square of {self.n} is {self.n*self.n}")
    def cube(self):
         print(f"cube of {self.n} is {self.n*self.n*self.n}")
    def squareroot(self):
         print(f"Square of {self.n} Root is {self.n**(1/2)}")
        
x = calculator(25)
x.square()
x.cube()
x.squareroot()