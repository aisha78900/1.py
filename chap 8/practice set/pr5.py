# ek pattern print kren 
# ***
# **
# *

def pattern(n):
    if(n==0):
        return "" #batt khtm kr deta hy jese hi condition match hota hy program end
    print("*"*n)
    pattern(n-1) #is se n n-1 bn jayega 
    
    
# print("*" * n) → line print hoti hai
# pattern(n - 1) → agli (chhoti) line print karne ke
# liye phir se function call hota hai

pattern(5)