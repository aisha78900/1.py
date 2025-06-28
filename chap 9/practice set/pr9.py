# hmne dekhna hy 2 files me content same hy ya nahi 

with open("file1.txt") as f:
    content1 = f.read()
    
with open("file2.txt") as f :
    content2 = f.read()
    
if (content1 == content2 ):
    print("both files are same")
    
else :
    print("not same")