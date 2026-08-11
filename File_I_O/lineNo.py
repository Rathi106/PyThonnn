with open("text.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("sristi" in line):
        print(f"sristi is in line {lineno}")
        break
    lineno += 1
else:
    print("sristi is not present")