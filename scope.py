#Local
lambda num:num+2

#Enclosing
name="Global scope"
print('Hello '+name)
def greet():

    name = 'Inner Global Scope'
    print('Hello '+name)

    def hello():
        name = 'Local Scope'
        print('Hello '+name)

    hello()

greet()


#Use of Global

x=50

def func():
    global x 
    print(f'X is {x}')

    x= 'New Value'
    print(f'I just locally changed global  x to {x}')

func()




