def fun():
  try:
    a = int(input("Hey,Enter a no. : "))
    print(a)
    return

  except ValueError as b:
    print("INVALID")
    print(b)
    return

  finally:
    print("Im inside finally")
    """Even if the function returns finally will still run"""

fun()
