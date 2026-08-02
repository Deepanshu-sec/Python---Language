#       Multiple Inheritance
class employe:
    company = "Meta"
    name = "Deepanshu"
    def show(self):
        print(f"Name = {self.name}, Company Name = {self.company}")

class coder:
      language = "Python"
      def printlang(self):
           print(f"Language Name = {self.language}")

class programer(employe,coder):
        company = "ITC infoTech"
        def showlang(self):
                print(f"Company = {self.company} Language = {self.language}")
a = employe()
b = programer()
b.show()
b.printlang()
b.showlang()
