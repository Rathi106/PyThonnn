n = int(input("Enter a no. : "))

product = 1

for i in range(1,n+1):
    product = product*i

print(f"Factorial of the no. {n} is {product}")