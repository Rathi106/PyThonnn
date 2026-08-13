class student:
    language = "py" #this is a class attribute
    salary = "20,00,000"

    @staticmethod
    def greet():
       print("Hemlo") 
    
    def getinfo(self):
     print(f"Name is {self.name}.The language is {self.language}. The salary is {self.salary}")

rathi = student()
rathi.name = "Rathi" 
rathi.greet()
rathi.getinfo()
# student.getinfo(rathi) "This is what the comp runs"
