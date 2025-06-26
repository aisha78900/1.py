# factorial find krna hy 
#factorial ye hota hy ke agr 5! = 1 x 2 x 3 x 4 x 5 
# mtlb 1 se le kr 5 tk sary number se mulitply krengy tw 5 ka factorial hoga 

n = int(input("Enter a number: "))
stored_product = 1

for i in range(1, n+1):
    saved_product = stored_product * i
    stored_product = saved_product #agr hm ek hi varaible use kren tw wo khud hi update hojaye like below 

print(f"Factorial of {n} is {stored_product}")


n = int(input("Enter the number: "))
product = 1
for i in range(1, n+1):
    product = product * i

print(f"The factorial of {n} is {product}")