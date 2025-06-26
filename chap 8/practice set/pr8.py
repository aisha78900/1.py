# multiplication table likhna hy using function of given number

def multi(n):
    for i in range(1 , 11):
        print(f"{n} x {i} is {n*i}")
        
n = int(input("enter your number :"))
multi(n)