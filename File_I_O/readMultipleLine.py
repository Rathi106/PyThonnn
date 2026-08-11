f = open("text.txt")

# lines = f.readlines()
# line1 = f.readline()


# print(lines,type(lines))
# print(line1,type(line1))

# f.close()

line = f.readline()

while(line != ""): #"" means an empty string
    print(line)
    line = f.readline() 

f.close()
