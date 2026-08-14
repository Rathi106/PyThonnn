try :
   with open("text.txt") as f:
       print(f.read)

except Exception as a:
    print(a)

try :
   with open("text2.txt") as f:
       print(f.read())

except Exception as a:
    print(a)

try :
   with open("text1.txt") as f:
       print(f.read)

except Exception as a:
    print(a)

print("Not Crashed!")