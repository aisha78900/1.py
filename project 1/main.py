import random

'''
water = -1
snake = 1
gun = 0

'''

computer = random.choice([-1,0,1])
youstr= input("enter your number: ") 
youdict= { "w": -1 , "g": 0 , "s": 1}
you = youdict[youstr] #hm apko key dengy tw ap dict se value le lena 
'''
[youstr] This is called getting a value from a dictionary using a key — or simply:
👉 "Dictionary lookup" using square brackets.

'''
reversedict = { -1: "water" , 1 :"snake" , 0 :"gun" }
#hmne key di in youstr or phr usne us key ki value le li from youdict
print(f"you chose {reversedict[you]} \ncomputer chose {reversedict[computer]}")
if(computer==you):
    print("It's a draw")
    
else:
    if(computer == -1 and you == 1):
        print("you win")
    elif(computer == -1 and you == 0):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 1 and you == -1):
        print("You lose")
    elif(computer == 0 and you == 1):
        print("You lose")
    elif(computer == 0 and you == -1):
        print("You win")
    else:
        print("something wnet wrong")
        
        
        
