
# factorial(5) = 1 x 2 x 3 x 4 x 5 
# Recursion means a function calling itself to solve a smaller part of a problem.


# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2 x 1
# factorial(3) = 3 x 2 x 1
# factorial(4) = 4 x 3 x 2 x 1

def factorial(n):
    if (n==1 or n==0):
        return 1 #yhan agr print use krty tw koi calc nahi hoti or agr hmne ye nahi lgaya tw recursionn kabhi sttop nahi hota or loop men chlta rehta hy ye lgana zrori hy
    return n * factorial(n-1)

n = int(input("enter ur num"))
print(f"the factorail of this number is {factorial(n)}")