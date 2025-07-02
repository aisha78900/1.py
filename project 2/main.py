from random import randint
a = -1
n = randint(1 , 100)
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Guess a number"))
    if (a>n):
        print("Lower number please")
    else:
        print("Higher number please")
        
print(f"You have guessed the number {guesses} attempt")