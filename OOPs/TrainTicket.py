from random import randint

class train:
    def __init__(self,trainno,fro,to):
        self.trainno = trainno
        self.fro = fro
        self.to = to

    def book(self,fro,to):
        print(f"Your Ticket for Train No. {self.trainno} from {self.fro} to {self.to} is booked sucessfully!")

    def status(self,fro,to):
        print(f"Train No. {self.trainno}  is running on time")

    def price(self,fro,to):
        print(f"Ticket price for your train {self.trainno} from {self.fro} to {self.to} is {randint(500,1000)}")


t = train(12323,"Howrah","Hindmotor")
t.book("Howrah","Hindmotor")
t.status("Howrah","Hindmotor")
t.price("Howrah","Hindmotor")

        