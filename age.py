age=float(input('enter age:'))
if age>0 and age<=18:
    print("You are a teenager")
elif age>18 and age<=60:
    print("You are working person")
elif age>60 and age<=100:
    print("You are retired")
else:
    print("Invalid age")

