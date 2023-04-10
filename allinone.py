def create_cube(n):
#    result=[]
#    for x in range (n):
#        result.append(x**3)
#    return result

   for x in range (n):
        yield (x**3)

for x in create_cube(10):
    print (x)


def my_function(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_function(1, 2, c="l", a=4, b=5)  # prints 1, 2, 3, "a: 4", "b: 5"


