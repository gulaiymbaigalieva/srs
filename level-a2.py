import re
num = '\d'
str = 'If 300 spartans were so brave, so 500 spartans could destroy more than 10k warriors of Darius, but 15k and even 20k.'
result=set(re.findall(num, str))
print(result)