import re
str =input("coilem:").max()
count=0
for i in str:
    if len(i)>count:
        count=len(i)
        word=i
print(" uzin coz:", word)
