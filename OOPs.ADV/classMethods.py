class student:
    a = 1 #class attribute
    @classmethod
    def show(cls):
        print(f"Value of a is {cls.a}") #it shows the class attribute not the instant attribute

m = student()
m.a = 106 #instant attribute
m.show()