def a(n):
    if(n == 1 or n == 0):
        return 1
    return n * a(n-1)

n = int(input("Enter a no. : "))
print(f"The factorial of this no. is : {a(n)}")

