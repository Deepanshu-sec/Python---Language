# Write a class train which has methods to book a ticket, get status(no. of seats) and get fare
# info of train running Under indian Railways.
from random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
    def book(self,fro,to):
        print(f"Ticket is booked train no. {self.trainNo} from {fro} to {to}")
    def status(self):
        print(f"Train no. {self.trainNo} is running on time")
    def info(self,fro,to):
        print(f"Ticket fare in Train no. {self.trainNo} from {fro} to {to} is {randint(200,1100)}")

x = train(71910)
x.book("deoband","New delhi")
x.status()
x.info("deoband","New delhi")