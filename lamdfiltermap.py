l1=[1,2,3,4,5,6,7,8,9,10]

l2=list(filter(lambda x : x%2==0,l1))

print(l2)

l3=list(map(lambda x:pow(x,2),l2))

print(l3)


print(list(filter(lambda x: x % 2 == 0, [11,12,11])))