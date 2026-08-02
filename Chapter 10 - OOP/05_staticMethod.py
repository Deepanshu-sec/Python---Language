class car:
    name = "BMW"
    model = "M5cs"
    
    def pro(self):
        print(f"The car is {self.name} The model is {self.model}")  # static method use nahi hoga bcz 
        # arguments pass ho rahe h..

    @staticmethod  # --> Decorater
    def func():   # staticMethod use kar sakte h BCZ arguments pass nahi ho rahe..
        print("Hello Good Morning !!!")

a = car()
a.func()
a.pro()
