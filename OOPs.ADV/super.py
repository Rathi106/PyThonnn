class employee: 
    def __init__(self):
        print("Its in employee")

class programm(employee):
    def __init__(self):
        print("Its in programm")

class python(programm):
    
    def __init__(self):
        super().__init__()
        print("Its in python")

m = python()


