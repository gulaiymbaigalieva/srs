import re
word="test"
str="This is a simple test message for test"
result=re.findall (word, str)
print (len(result))