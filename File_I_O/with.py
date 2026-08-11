# f = open("text.txt")

# print(f.read())

# f.close

#same can be done using with statement
with open("text.txt") as f:
    print(f.read())

#now u don't have to close the file