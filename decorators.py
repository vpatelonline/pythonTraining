#Decorators - extend the functionality of some function or class

#Zero division error
#def div(a,b):
    #return a/b

#print(div(5,0))

#Decorators - 1

def verify(func):
    def inside(a,b):
        if b==0:
            print("Can't divide by 0")
            return
        func(a,b)
    return inside


@verify
def div(a,b):
    return a/b

print(div(5,0))

#Decorators - 2


def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))


#Decorators - 3


def sub_markets(func,sub_market_type):
    if sub_market_type == 'NASDAQ':
        def sub_market_nasdaq():
            func()
            print("Clients requirment related to NASDAQ has been staisfied")
            print("Clients additional requirment added to NASDAQ")
        return sub_market_nasdaq
    elif sub_market_type == 'SP500':
        def sub_market_SP500():
            print("Clients requirment related to SP500 has been staisfied")
        return sub_market_SP500
    else:
        print("Submarket type requirment not implemented")
        


for sub_market_type in ['NASDAQ','SP500','XYZ']:
     
    def main_market():
        print("Clients requirment related to main market has been staisfied")
    
    main_market = sub_markets(main_market,sub_market_type)
    
    if main_market is None:
        print('***Alert***: Please implement necessary Submarket type')
    else:
        main_market()


def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result) 


def make_pretty(func):
    # define the inner function 
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        func()
    # return the inner function
    return inner

# define ordinary function
def ordinary():
    print("I am ordinary")
    
# decorate the ordinary function
decorated_func = make_pretty(ordinary)

# call the decorated function
decorated_func()





