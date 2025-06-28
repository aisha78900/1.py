# isme word donkey ko replace krna hy 
word = "donkey"

with open("donkey.txt" , "r") as f:
    content = f.read()
    
contentNew = content.replace(word, "monkey")

with open("donkey.txt", "w") as f:
    f.write(contentNew)