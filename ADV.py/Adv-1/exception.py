try:
   a = int(input("Hey,Enter a no. : "))
   print(a)

except ValueError as b:
   print("INVALID")
   print(b)

except Exception as e:
   print(e)


print("Thank You!")
