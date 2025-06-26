d = {} # Empty dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}


# print(marks, type(marks))
# print(marks["Harry"])
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99 , "ayesha" : 200}) #jo hen wo update hojayengy jo nahi hen wo add hojayngy
# print(marks)

# print(marks.get("Harry")) 
# marks.pop("56")
# print(marks) #jo value doge wo hta dega

marks.popitem()
print(marks)  #last item ko hta dega