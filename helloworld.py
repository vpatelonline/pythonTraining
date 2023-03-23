print('1: Hello World')
print("2: Hello World")
print('3: Hello+World')
print('4: Hello/World')
print('5: Hello''World')
print('6: Hello' ""  'World')
print('7: Hello' " "  'World')
print('8: Hello#World')
print('9: Hello\
World')
print('10: Hello'\
'World')


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
