a = "icecream"
b = "potato"
c = "chini"

message = input("Enter your message : ")
if((a in message) or (b in message) or (c in message)):
    print("Its a spam message")

else:
    print("Valid message")