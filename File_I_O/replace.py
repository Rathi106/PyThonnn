import re

with open("text.txt") as f:
    content = f.read()

contentnew = re.sub(r"Mohobbat", "Laude", content, flags=re.IGNORECASE)

with open("text.txt","w") as f:
    content = f.write(contentnew)
