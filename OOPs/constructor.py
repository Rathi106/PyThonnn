class student:
    language = "py" 
    salary = "20,00,000"

    def __init__(self,name,salary,language): # dunder method which is automaticaly called
       self.name = name
       self.salary = salary
       self.language = language
       print("Here we go!!!!")
                      
    @staticmethod
    def greet():
       print("Hemlo") 
    
    def getinfo(self):
     print(f"Name is {self.name}.The language is {self.language}. The salary is {self.salary}")

rathi = student("Rathi",1200000,"JavaScript")
# rathi.name = "Rathi" 
print(rathi.name,rathi.language,rathi.salary)