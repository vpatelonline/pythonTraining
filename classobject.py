class GrandFather():
    def house (self):
        print('This is a GrandFathers house')
    
class Father(GrandFather):
    def house2 (self):
        print('This is a Fathers house')

class Son(Father):
    def house1 (self):
        print('This is a sons house')

g=GrandFather()
f=Father()
s=Son()

s.house()













