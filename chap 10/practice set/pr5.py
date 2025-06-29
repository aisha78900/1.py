from random import randint 
# write a class train which has mehtods book a ticket , get fare , status (train is working or not)
 


class train:
     def book(self , trainno , fro , to ):
         print(f"ticket is book train No {trainno} from {fro} to {to}")
     def status(self , trainno):
         print(f"Train {trainno} is working")    
     def getfare(self , trainno , fro , to):
         print(f"train No {trainno} from {fro} to {to} is of {randint(222, 7000)}")

         
train = train()
train.book("12" , "KARACHI" , "LAHORE")
train.status("12")
train.getfare("12" , "KARACHI" , "LAHORE")