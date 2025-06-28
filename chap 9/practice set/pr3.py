def generateTable(n):
    table = " "
    for i in range(1 , 11):
        table += f"{n} X {i} = {n*i}\n"       #table += ka mtlb hy ke table ek khali variable hy jb jb loop chly ga usme new add krdena line 
                        #+= ka matlab hai pehli value ke saath nayi value jodna.
    with open (f"tables/table_{n}.txt" , "w") as f:
        f.write(table)
        
for i in range (2 , 21):
    generateTable(i)
  
  
  
# is problem me hmen tables print krwany hen new files men sari ``