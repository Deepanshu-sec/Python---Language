class employe:
    name = "Deepanshu"
    language = "Python"
    salary = 50
    def __init__(self,name,language,salary): # --> Constructor(dunder method)
        self.name = name
        self.language = language
        self.salary = salary 
        print("I am immortal")

    def func(self):
        print(f"Name = {self.name} Language  = {self.language} salary = {self.salary}")

a = employe("Harvey Specter","JAVA",99999)
print(a.name,a.language,a.salary)
# a.func()


