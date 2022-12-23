text="my phone number is (862) 233-456"
print('phone' in text)

import re

pattern='call'
print(re.search(pattern,text))

pattern='phone'
match = re.search(pattern,text)
print(match)

print(match.span())
print(match.start())
print(match.end())

text = 'call me on this or call me on this'
pattern = 'call me'
print(re.search(pattern,text))  #Just find first occurance
print(re.findall(pattern,text))  # All occurance


for match in re.finditer('call me',text):
    print(match)
    print(match.span())
    print(match.group())

