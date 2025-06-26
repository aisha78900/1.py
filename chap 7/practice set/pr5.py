# ek esa program bnana hy 
# jo hm input den tw sary 
# number jo us se pehly ke hen add kr 
# de like agr hm 5 den tw wo 1 ko sum 
# men add kre phr 2 ko 1 men add kre phr 
# 3 ko us men add kre phr 
# tb tk chly jb tk i = n na hojaye 


n = int(input("enter your number: "))

i = 1
sum = 0

while(i<=n):
    sum = sum + i #yhan isne sum men i ko plus kia 
    i = i + 1 # yhan isne 1 men 1 ko plus kia (value yhan brhti jayegi jb tk i = n na ho)
    
print (sum) 
