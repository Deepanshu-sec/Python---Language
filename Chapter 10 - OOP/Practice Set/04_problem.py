# Add a static method in problem 2, to greet the user with hello.
class calculator:
    def __init__(self,n):
        self.n = n
    def square(self):
         print(f"Square of {self.n} is {self.n*self.n}")
    def cube(self):
         print(f"cube of {self.n} is {self.n*self.n*self.n}")
    def squareroot(self):
         print(f"Square of {self.n} Root is {self.n**(1/2)}")
    @staticmethod
    def greet():
         print("Hello!!!! there...")
x = calculator(5)
x.greet()
x.square()
x.cube()
x.squareroot()