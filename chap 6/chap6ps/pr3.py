p1 = "I am human"
p2 = "i am robot"

msg = input("Enter your message: ")

if (p1 in msg) or (p2 in msg):
    print("Spam")
else:
    print("Not Spam")