class student:
    a = 1 

    @classmethod
    def show(cls):
        print(f"Value of a is {cls.a}") 

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self,value):
        self.lname = value.split(" ")[0]
        self.fname = value.split(" ")[1]


m = student()
m.name = "Rathi Manmohan"
print(m.fname,m.lname)