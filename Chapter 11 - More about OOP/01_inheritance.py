# class employe:
#     company = "Galaxy"
#     name = "Deepanshu"
#                                    # sirf name change karne k liye itna bda code.||
#     def show(self):
#         print(f"name is {self.name} company = {self.company}")
# class student:
#     company = "Apple"
#     name = "Harvey Specter"
#     def show(self):
#         print(f"name is {self.name} company = {self.company}")
#           USE SINGLE INHERITANCE
class employe:
    name = "Deepanshu"
    company = "Meta"
    def show(self):
        print(f"Name {self.name} Company = {self.company}")
class student(employe):
    name = "Harvey"
    company = "Pearson Hardman"

# a = employe()
# a.show()
b = student()
b.show()
