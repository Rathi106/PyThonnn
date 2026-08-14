from functools import reduce
#Map examle
l = [1,2,3,4,5]

square = lambda x:x*x

squarelist =map(square,l)

print(list(squarelist))

#Filter example
def even(n):
    if(n%2 == 0):
        return True

onlyeven = filter(even,l)
print(list(onlyeven))

#Reduce example
def sum(a,b):
    return a +b

def multiply(a,b):
    return a*b

print(reduce(sum,l))

print(reduce(multiply,l))