# write a program to give a multiplication table of given number 

n = int(input("enter your number: "))
for i in range (1 , 11):
    print(f"{n} X {i} = {n*i}")