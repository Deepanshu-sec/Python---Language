class demo:
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return self.fname
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = demo()
e.a = 5
e.name = "Deepanshu rana"
print(e.fname, e.lname)
e.show()