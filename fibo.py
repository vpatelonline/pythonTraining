n=int(input("Fibo up to: "))
n0=0
n1=1
count=0
if n<=0:
    print("No Fibo. Please Enter positive number")
elif n==1:
    print(n1)
else:
    
    while count<n:
        print(n0, end=', ')
        nth=n0+n1
        n0=n1
        n1=nth
        count+=1
