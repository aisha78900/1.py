# isme dekhna hy python hy file me ya nahi 
with open("pr6.txt") as f:
    content = f.read()
    
if("python" in content):
    print("yes")