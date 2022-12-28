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

text = 'call me on 123-456-7890 this or call me on 987-654-3210'
pattern = 'call me'
print(re.search(pattern,text))  #Just find first occurance
print(re.findall(pattern,text))  # All occurance


for match in re.finditer('call me',text):
    print(match)
    print(match.span())
    print(match.group())

print('\n')
phone=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)

print('\n')
phone=re.findall(r'\d\d\d-\d\d\d-\d\d\d\d',text)
print(phone)

print('\n')
phone=re.search(r'\d{3}-\d{3}-\d{4}',text)
print(phone)

print('\n')
phone=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
print(re.search(phone,text))

print('\n')


text='The cat in the hat went splat'
print(re.findall(r'.at',text))
print(re.findall(r'..at',text))
print(re.findall(r'...at',text))

print(re.findall(r'^\d','1 is a number'))



