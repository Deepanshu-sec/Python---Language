class student:
    name = "Deepanshu"
    salary = 10000000
    age = 18
    def func(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    def greet(self):
        print("Good Morning")

a = student()
a.name = "Harvey Specter"
a.greet()
a.func()

b = student()
b.name = 'Jon snow'
b.salary = "The king in the north"
b.func()
