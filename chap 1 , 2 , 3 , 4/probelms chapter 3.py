name = input("enter your name: ")
print(f"good afternoon {name}")

# problem 2
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Harry").replace("<|Date|", "24 September 2050"))


name = "Harry is a good  boy and  "

print(name.replace("  ", " "))
print(name)

