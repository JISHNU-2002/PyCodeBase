import re
p = "\d\d\d\d\d\d\d\d\d\d"
t = "my number is 9605256697"
match = re.search(p,t)

if match : 
    print("match found : ",match.group())
else :
    print("no match")

pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)
