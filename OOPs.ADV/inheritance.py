class employee: #Its the parent class
    company = "ITC"
    name = "Rathi"
    def show(self):
        print(f"Name is {self.name} and his salary is {self.company}")

class coder: #parent class
    language = "Py"
    def printlanguage(self):
        print(f"Out of all the languages your language is : {self.language}")

class programmer(employee,coder) : #It is the same thing and it becames the inherit class
    company = "ITC infotech."
    def showlanguage(self):
        print(f"The name is {self.company} and he is good in language {self.language} language")


a = employee()
b = programmer()

print(a.company, b.company)
a.show()
b.printlanguage()
b.showlanguage()