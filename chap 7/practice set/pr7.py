# hmen ek pattern ko bnana hy jo bhii number 
# den utni lines men wo star ka
# pattern bn jaye like below
# (agr n= 3 hy tw)

#   *
#  ***
# ***** 



    
n = int(input("enter your number: "))
for i in range(1 , n+1):
    print(" "*(n-i) , end=" ")
    #hmne yhan end is lie lgaya
    # hy ke ye new line nahi bnayega
    # space ki bhi or star ki bhi tw 
    # jb hmne 1st row print krwai jb 
    # i = 1 hoga tw dono
    # ek line men ayengy 
    print("*"*(2*i-1), end=" ")
    print(" ")
    
# n = 3 
# 3 - i(1) = 2 
#   two space

# phr dosra print
# 2 x 1 -1 = 1 
# tw ek star 

# 3 -i(2) = 1
# 1 gap 

# 2 x 2 - 1 = 3 
# tw 3 star

