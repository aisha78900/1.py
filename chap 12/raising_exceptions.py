# is me ye hota hy ke hm ek error de dety hen custom ke agr esa hwa tw tm erro de dena 

a = int(input("enter your number : "))
b = int(input("enter your number : "))

if (b == 0):
    raise ZeroDivisionError("Hey you cant divide by zero in python")

else:
    print(f"the divide is {a/b}")