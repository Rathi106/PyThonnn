try:
   a = int(input("Hey,Enter a no. : "))
   print(a)

except ValueError as b:
   print("INVALID")
   print(b)

else:
   print("Im inside else")
   """"itll only run if the try is sucess"""