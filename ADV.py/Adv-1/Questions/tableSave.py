a = int(input("Enter a no. : "))

table = [a*i for i in range(1,11)]
print(table)

with open("table.txt","a") as f:
    f.write(f"Table of {a} : {str(table)} \n")
