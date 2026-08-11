with open("text.txt") as f:
    lines1 = f.readlines()

with open("new_text.txt") as f:
    lines2 = f.readlines()

if(lines1 == lines2):
    print("Files are identical")

else:
    print("Files are not identical")