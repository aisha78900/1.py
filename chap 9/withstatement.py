f = open("file.txt")
print(f.read())
f.close()

#isko hm ese bhi likh skty hen or hmen close nahi lgana prega 
with open("file.txt") as f:
    print(f.read())
    
#you dont need to use close here