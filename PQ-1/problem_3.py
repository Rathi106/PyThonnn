import os

# select teh directory whose content u want to list
# use the os module to ist the directory content
contents = os.listdir("C:\\Users\\PC\\Desktop\\spam")

# print the contents of the directory
for item in contents:
    print(item)
    