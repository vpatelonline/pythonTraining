#Python Decorator Example:

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(x, y):
    return x + y

result = add(2, 3)
# Output: Calling function add with args (2, 3) and kwargs {}
#         5



#Python Generator Example:
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i in range(10):
    print(next(fib))
# Output: 0 1 1 2 3 5 8 13 21 34



def fancy_fun(func):
    def wrapper():
        print("Before calling simple_fun")
        func()
        print("After calling simple fun")
    return wrapper
        
@fancy_fun   
def simple_fun():
    print("I am simple")



    

