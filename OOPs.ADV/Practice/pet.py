class animal:
    pass

class pets(animal):
    pass

class dog(pets):
    @staticmethod
    def bark():
        print("bhow bhow")

a = dog()
a.bark()
