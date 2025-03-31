# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways. 
import random
class Train:

    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"Ticked is booked in train no: {self.trainNo} from {fro} to {to}")

    def status(self):
        print(f"Train no: {self.trainNo} is running on time")

    def fare(self,fro,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {random.randint(222,555)}")

t=Train(12281)
t.book("Jhansi","Delhi")
t.status()
t.fare("Jhansi","Delhi")

        

