# isme hmen ek kam krna hy ke 3 4 words hen unko replace krna hy 
words = ["donkey" , "monkey" , "bnana",  "elephant" ]

with open("pr5.txt") as f:
    content= f.read()
    
for word in words:
    content =content.replace(word , "#" *len(word))
    
with open("pr5.txt" , "w") as f:
    f.write(content)