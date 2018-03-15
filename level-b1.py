import re
num = '[\d\-]+'
str = 'The temperature can be in range 10-15C next week though it was lesser last week(4-9C).'
result=re.findall(num, str)
print(result)