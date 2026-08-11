s = open("text.txt")

content = s.read()

if("sristi" in content):
    print("sristi is present")

else:
    print("sristi is not present")