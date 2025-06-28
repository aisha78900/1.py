# hmen ek file lani hy jis ko rename krna hy 

with open("old.txt") as f :
    content2 = f.read() 
    
with open("renamed_by_python" , "w") as f :
    f.write(content2)