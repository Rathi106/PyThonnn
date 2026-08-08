#it is mutable
d = {} # empty dictionary
marks = {
    "rathi" : 67,
   "mohobbat" : 87,
   "sristi" : 76
}
# print(marks,type(marks))
print(marks["mohobbat"]) # returns an error
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"rathi" : 99,"bhaila": 60})
# print(marks)
print(marks.get("rathi")) # prints none
