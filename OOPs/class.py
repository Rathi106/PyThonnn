class student:
    language = "py" #this is a class attribute
    salary = "20,00,000"  

rathi = student()
rathi.name = "Rathi" #it's an object attribute
print(rathi.name,rathi.language,rathi.salary)

mohobbat = student()
mohobbat.name = "Mohobbat"
print(mohobbat.name,mohobbat.language,mohobbat.salary)

'''here name is the object/instant attribute and salary and language is the
 class attribute since they directly belongs to the class '''

sristi = student()
sristi.name = "sristi"
sristi.language = "java script"
print(sristi.name,sristi.language,sristi.salary)

'''instant attribute is more preferable then class attribute'''