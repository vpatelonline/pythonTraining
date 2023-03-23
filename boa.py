my_dict ={"Java":100, "Python":112, "C":11}
print(my_dict.keys())
print(my_dict.values())
print('\n')
print(list(my_dict.keys()))
print(list(my_dict.values()))
print('\n')
print(list(my_dict.keys()).index("C"))
print(list(my_dict.values()).index(112))
print('\n')
print(type(my_dict))
print('\n')
# one-liner
print("One line Code Key value: ", list(my_dict.keys())[0])
print("One line Code Key value: ", list(my_dict.keys())[list(my_dict.values()).index(100)])






def outer(x):
    def inner(y):
        return x + y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)






























    
    
    

