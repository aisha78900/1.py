# hmen 3 sub ke marks lene hen student se or percent nikalna hy agr uska percent 40 se km hwa 
# tw hmne fail btaana hy or nahi tw pass 
# Write a program to find out whether a student
# is pass bro' fail if it regires total 40% and
# st least 33), in each subject to pass. Asune
# 3 Sulyects and take morks as an input from the user

m1=int(input("enter num 1 :"))
m2=int(input("enter num 2 :"))
m3=int(input("enter num 3 :"))

total_percent=((m1 + m2 + m3 )/300)*100

if(total_percent>=40 and m1>33 and m2>33 and m3>33 ):
    print("u are passed " , total_percent) 
    
else:
    print("u are fail" , total_percent)
    
    
