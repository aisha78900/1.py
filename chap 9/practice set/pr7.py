# isme dekhna hy python  kis line me aya hy

with open("pr6.txt") as f:
  lines = f.readlines()
  
lineno = 1
for line in lines:
    if("python" in line):
        print(f"yes {lineno}")
        break 
    lineno += 1 
    
    
else:
    print("No Python is not present")