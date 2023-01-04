d={'k1':1,'k2':2,'k3':3}
print({x:x**2 for x in range(10)})
print({k:v**2 for k,v in zip(['a','b','c'],range(3))})

for x in d.items():
    print(x)

for x in d.keys():
    print(x)

for x in d.values():
    print(x)
