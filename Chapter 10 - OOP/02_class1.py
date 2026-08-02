class employee:
    name = "Deepanshu"     # --> This is the class attributes.
    language = "Python"
    salary = 100000

a = employee()
a.name = 'Deepanshu'    # --> This is the object(instance) attribute.
print(a.name,a.language,a.salary)

b = employee()
b.name = 'Harvey Specter'
print(b.name,b.salary,b.language)
