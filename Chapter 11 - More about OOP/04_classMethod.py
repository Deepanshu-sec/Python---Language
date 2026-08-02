class demo:
    n = 1
    @classmethod   # ab instance attribute print nahi hoga.
    def func(cls):
      print(f"class attribute is {cls.n}")

a = demo()
a.n = 5    
a.func()
