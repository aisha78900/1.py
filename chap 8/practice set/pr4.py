# find a recursive function to calculate the sum of first n nayural number

# sum(1)= 1
# sum(2)= 1+2
# sum(3)= 1+2 +3
# sum(n)= 1+2 +3 +n 
# sum(n)= sum(n-1)
def sum_natural(n):
    if(n==1):
        return 1 #ye base condition hy 
    return n + sum_natural(n-1)

b = int(input("enter number: "))
print(sum_natural(b))


# agr hmne 4 dia tw pehly wo krega sum of 4 + 3 phr wo 3 ko 3 + 2 krega phr jb 1 pr jayega tw stop hojayega 