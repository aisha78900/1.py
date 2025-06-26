def inch_to_cms(inch):
    return inch*2.54

n = int(input("enter your number: "))
print(f"{n} inches = {inch_to_cms(n)}")