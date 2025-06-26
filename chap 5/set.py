# # How to make empty set 
# set = set()
# # q ky dictoanry or sets dono curly brackets men bnty
# # hen tw islie hm empty set ese bnaty hen 

# set ={ 1 , 3 , 5 , 5, 5 , "ayesha"}
# print(set)

# # set ki khas baat ye hy ke isme koi bhi same value repaet nahi hogi like 5 in above 

# # Methods
# set.add(33)
# print(set)
# set.remove(33)
# print(set)

# sets are unindexed mtlb hm inko [0,1] kr ke call nahi kr skty
# koi bhi order nahi hota set ka

# UNION IN SET
s1= {1 , 2 , 3 , 4 }
s2={ 1 , 2 , 5 , 5 , 8 , 3}
# j = s1.union(s2) #sary de do 
# print(j)


# # Intersection 
# j = s1.intersection(s2)
# print(j) #jo same hen wo de do

# print(s1-s2)
# print(s2-s1)


# Item remove karta hai (error nahi deta agar item na ho).
s1.discard(10)

# Ek ya zyada items ek sath add karta hai.
s1.update([6, 7])
print(s1)


# Jo a me hain lekin b me nahi.
print(s1.difference(s2))

# Check karta hai kya a set b ka subset hai.

s4 = {1, 2 , 4 , 9 , 10, 44}
s3 = {1, 2, 3 , 5 , 8 ,}
print(s4.issubset(s3)) 


# Check karta hai kya a set b ka superset hai.
print(s3.issuperset(s4)) 

# Wo items jo sirf ek hi set me hon (common nahi).

print(s4.symmetric_difference(s3))

result = sorted(s3.symmetric_difference(s4))
print(result)