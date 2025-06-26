tuple = (1, 2 , 3 , 4, 5 , 5) #tuple are immutable 
# agr hmen ek 1 element wala tuple bnanaa ho tw hm (1,) ese bnaygy 



# ----------------- Method---------------------

no = tuple.count(5)
print(no)
i = tuple.index(5)
print(i)

# -----------------------------------OPERATIONS--------------------------------

# --------------- concatinate -----------------------
t1 = (1, 2)
t2 = (3, 4)
result = t1 + t2  # (1, 2, 3, 4)
print(result)


# --------------Repetition (*)------------------
t = (1, 2)
result = t * 3  # (1, 2, 1, 2, 1, 2)
print(result)

# -----------------------Membership (in, not in)--------------------
t = (1, 2, 3)
print(2 in t)       # True
print(4 not in t)   # True

# -------------------Indexing--------------------
t = (10, 20, 30)
print(t[1])  # 20

# ------------------Slicing----------------
t = (0, 1, 2, 3, 4)
print(t[1:4])  # (1, 2, 3)


# ---------------------Length (len())--------------------------
t = (1, 2, 3)
print(len(t))  # 3

# ------------------------Iteration (for loop)---------------------
t = (5, 6, 7)
for item in t:
    print(item) #YE SARY ITEMS KO PRINT KR DEGA 
    
    
    
    
# -----------------------Nested Tuples--------------------
    
t = ((1, 2), (3, 4))
print(t[1][0])  # 3

# Isme index 1 pr dosra tuple hy or uske pehly indes pr 3 hy , 
# mtlb dosry tuple ka pehla number outuput hoga 
# 
#  t[1] → (3, 4) → dusra tuple
# (3, 4)[0] → 3 → uska pehla number

