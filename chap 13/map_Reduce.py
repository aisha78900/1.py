
from functools import reduce
# map agr hmen ek func chalana hy sary item pr 

l = [1 , 2 , 3 , 4 , 5]
sq = lambda x:x*x
sqlist = map(sq , l)
print(list(sqlist))

# filter example 
def even(n):
    if (n%2 == 0):
        return True
    
onlyeven = filter(even , l)
print(list(onlyeven))

#reduce example
def sum(a , b):
    return a+b


print(reduce(sum ,l))

# ye ese chlega mtlb pehly 1+ 2 phr + 3 + phr 4 ese 