# try else men ye hota hy ke agr hm successfully oper 
# waly code ko chla paye tw hmen else mil
# jayega wrna wo error any pr whi stop hojan 
try:
    a = int(input("Enter your number: "))
    print(a)
    
except Exception as e:
    print(e)
    
else:
    print("Int is working") #isme jb ayega jb try successful ho