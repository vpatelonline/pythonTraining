x=[1,2,3]
x.append([4,5])
print(x)

x.pop()
print(x)

x.extend([4,5])
print(x)

print(x.index(5))

x.insert(2,'abcd')
print(x)

x.pop(2)
print(x)

x.remove(4)
print(x)

y=[1,2,3,4,3,4]
y.remove(3)
print(y)

y.reverse()
print(y)

y.sort()
print(y)
