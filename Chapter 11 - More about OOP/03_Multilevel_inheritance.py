class harvey:
    def __init__(self):
        print("Constructor of harvey:")
    a = 1
class deep(harvey):
    def __init__(self):
            print("Constructor of deep:")
    b = 2
class owner(deep):
       def __init__(self):
         print("Constructor of owner:")
         super().__init__()
       c = 3

x = harvey()
print(x.a)

y = deep()
print(y.a,y.b)

z = owner()
print(z.a, z.b, z.c)
