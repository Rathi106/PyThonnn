a = int(input("Enter a no. : "))
b = int(input("Enter a no. : "))
# c = int(input("Enter a no. : "))

if(b == 0):
    raise ZeroDivisionError("0 is invalid!")

else:
 print(f"The division of {a}/{b} is {a/b}")