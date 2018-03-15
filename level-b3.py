import re
things = ['"Table" "1" "200 $"', '"Stool" "2" "100 $"', '"Mirror" "3" "400 $"']
kn = re.compile('".*?"')
result = []
for line in things:
  result.append(kn.findall(line))
print(result)