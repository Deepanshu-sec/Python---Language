# create a class "programmer" for storing info of few programmers working at Microsoft.
class programmer:
    def __init__(self,name,id):
        print("Company Microsoft")
        self.name = name
        self.id = id
    def func(self):
        print(f"Name = {self.name}, ID = {self.id}")

a = programmer("Deepanshu",1234)
a.func()
b = programmer("Harvey Specter",5678)
b.func()
c = programmer("Jon Snow",1100)
c.func()

         