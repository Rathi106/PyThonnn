class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def show(self):
        print(f"Coordinates of the 2D vector are {self.i}i + {self.j}j")

class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"Coordinates of the 3D vector are {self.i}i + {self.j}j + {self.k}k" )
        

a = TwoDvector(2,3)
a.show()
b = ThreeDvector(5,6,2)
b.show()