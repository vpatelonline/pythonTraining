thislist=["orange","banana","mango","kela","xxxx","uuuu"]
print(thislist)
thislist1=["orange1","banana1","mango1",1,9.7]
thislist2=thislist+thislist1
print(thislist2)
print(len(thislist2))
thislist3=list(())

if "orange" in thislist:
    print ('yes')
print(thislist[3:6])
thislist[3]='ccccc'
print(thislist)


thislist.insert(2,'lxxxx')
print(thislist)

thislist.remove("xxxx")
print(thislist)
thislist.pop(1)
print(thislist)
del thislist[0]
print(thislist)
del thislist
