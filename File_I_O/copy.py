with open("text.txt") as f:
    s = f.read()

with open("new_text.txt","w") as f:
    f.write(s)