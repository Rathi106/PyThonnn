class employee: 
    a = 1

class programm(employee):
    b = 2

class python(programm):
    c = 3

m = python()
print(m.a,m.b,m.c)
