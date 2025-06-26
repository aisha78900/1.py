# write a program using funt to fing greates of three number 
def greaternumber():
    if(a > b and a>c ):
        print(f"{a} is greater")
    elif(b>a and b>c):
        print(f"{b} is greater")
    elif(c>a and c>b):
        print(f"{c} is greater")
    return "done"

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))

greaternumber()
    