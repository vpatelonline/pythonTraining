def add(*args):
    ans=0
    for i in args: ans +=i
    return ans

print(__name__)
if __name__=='__main__':
    print(add(1,2,3))

