class employe:
    language = "Python"
    salary = 50
    def __init__(self): # --> Constructor(dunder method)
        print("I am immortal")

    def func(self):
        print(f"Language Name = {self.language} salary = {self.salary}")

a = employe()
a.language = "Java"
a.func()

b = employe()
