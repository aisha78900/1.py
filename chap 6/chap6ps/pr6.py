# program to cal grade of student from following scheme
# 90-100=>Ex
# 80-90 A
# 70-80 B
# 60-70 C
# 50-60 D
# <50 F

marks = int(input("Enter your marks: ")) 

if(marks<=100 and marks>=90 ):
    grade= "A"
elif(marks<90 and marks>=80 ):
    grade= "B"
elif(marks<80 and marks>=70 ):
    grade= "C"


print ("your grade is " , grade)
