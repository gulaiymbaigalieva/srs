import re
kn = 'ruby|java|python|c#'
str = 'ruby python 456 java 789 j2not clash2win'
result=re.findall(kn, str)
print(result)