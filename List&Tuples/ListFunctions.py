friend = ["hehe", 321,3.22,"mohobbat","sristi",False,"manmaohanaa"]

print(friend[3])
friend[0] = "grape" #unlike strings list are mutable(changeble)
print(friend[0])
print(friend[0:4])
friend.append("harry") #add
print(friend)

L1 = [21,33,1,33,11,44,1,106]

L1.sort()
print(L1)
L1.reverse()
print(L1)
L1.insert(6,6107) #insert 6107 such that its ndex in the list is 6
print(L1)
L1.pop(7) 
print(L1)
print(L1.pop(2))
print(L1)