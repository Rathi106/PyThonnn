class calculator:
    def __init__(self,n):
        self.n = n

        def square(self):
            print(f"Square of the no. {self.n} is {self.n*self.n}")
        def cube(self):
            print(f"Cube of the no. {self.n} is {self.n*self.n*self.n}")
        def squareroot(self):
            print(f"Squareroot of the no. {self.n} is {self.n**1/2}")


a = calculator(int(input("Enter your no. : ")))
a.square()
a.cube()
a.squareroot()
