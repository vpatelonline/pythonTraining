#def = Keyword to define a function, 
# Function name using snake casing - all lowercase and underscore between words
# Parenthesis - to pass argument/parameters
# Colon - indictaes the upcoming indentation
# Docstring using triple '''.

def my_first_function():
    ''' Function to print a statement '''
    print('This is my first function')

my_first_function()

def say_hello():
    ''' Function to pront hello, how are you?'''
    print('\nHello')
    print('How are you?')

say_hello()


def say_hello(name):
    print(f'\nHello {name}, How are you?')

say_hello('VP')


def print_name(name):
    ''' Function that print a name '''
    print("\nHello "+name)

print_name('VP')


def print_result(a,b):
    print(a+b)

print_result(9,10)

def return_result(a,b):
    return a+b

#This statement will not print the result as there is no print statement in function.
return_result(7,10) 

#These statement will print the result as we are calling the function and returing result will be stored in result variable.
result=return_result(7,10)
print(result)


def sum_two_numbers_1(a,b):
    ''' Function to add two numbers - method 1'''
    sum=a+b
    return(sum)

print(sum_two_numbers_1(5,6))


def sum_two_numbers_2(a,b):
    ''' Function to add two numbers - method 2'''
    return a+b

print(sum_two_numbers_2(7,6))


def sum_two_numbers_3(a,b):
    ''' Function to add two numbers - method 3'''
    return a+b

sum = sum_two_numbers_2(8,10)
print(sum)


def even_check(num):
    ''' Even number checker'''
    return num%2==0

print(even_check(10))



def even_in_list_1(my_list):
    '''If even number in list - print TRUE - Method 1'''
    for x in my_list:
        if x%2==0:
            print('TRUE')
            break
        else:
            pass
            
even_in_list_1([1,2,3,4,5,6])


def even_in_list_2(mylist1):
    '''If even number in list - print true - Method 2'''
    for number in mylist1:
        if number % 2 ==0:
            return True
        else:
            pass

print(even_in_list_2([1,2,3,4,5,6]))

even_num=[]
def list_even(my_list):
    '''Return list of even numbers'''
    for num in my_list:
        if num%2==0:
            even_num.append(num) 
        else:
            pass
    return even_num
            
print(list_even([1,2,3,4,5,6]))


# How to use lambda
li = [1,2,3]
new = list(map(lambda x:x+1, li))
print(new)


