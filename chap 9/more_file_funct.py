f = open("file.txt")
# realines ek function hy jis se o list me sari lines print kr deta hy 

# lines = f.readlines()
# print(lines , type(lines))

#f.readline ka function jitni bar chlayegy line print krega

# line1 = f.readline()
# print( line1  , type(line1))
# line2 = f.readline()
# print( line2  , type(line2))
# line3 = f.readline()
# print( line3  , type(line3))
# line4 = f.readline()
# print( line4  , type(line4))
# line5 = f.readline()
# print( line5 )
line = f.readline()

while(line != ""):
    print(line)
    line=f.readline()
f.close()