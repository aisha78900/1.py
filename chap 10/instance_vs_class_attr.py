# instance attribute agr likha ho tw wo pehly waly lass attribute ko over write kr deta hy means ke hta kr khud ajata hy 
class employee :
    lang = "py"
    salary = 12000
    
rohan = employee()
rohan.name = "rohan" # this is instance attribute
rohan.lang = "java"
print(rohan.name , rohan.salary , rohan.lang)
