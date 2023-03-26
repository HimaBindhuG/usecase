"""stri="HimA"
count=0
for i in stri:
    if i.isupper():
        count+=1
print(count)
"""
"""stri="HimA"
count=0
for i in stri:
    if (i>='A' and i<='Z'):
        count+=1
print(count)"""

stri="12321"

rev=stri[::-1]
if stri==rev:
    print("pali")
else:
    print("not pali")



