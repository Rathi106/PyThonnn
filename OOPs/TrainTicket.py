from random import randint

class train:
    def __init__(self,trainno,fro,to):
        self.trainno = trainno
        self.fro = fro
        self.to = to

    def book(self):
        print(f"Your Ticket for Train No. {self.trainno} from {self.fro} to {self.to} is booked sucessfully!")

    def status(self):
        print(f"Train No. {self.trainno}  is running on time")

    def price(self):
        print(f"Ticket price for your train {self.trainno} from {self.fro} to {self.to} is {randint(500,1000)}")


t = train(12323,"Howrah","Hindmotor")
t.book()
t.status()
t.price()

        