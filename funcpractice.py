
#LESSER OR GREATER:
def lesserevennum(a,b):
    '''this function return the lesser of two given numbers if both numbers are even, but return the greater if one or both numbers are odd'''
    if a%2==0 and b%2==0:
        if a>b:
            return b
        else:
            return a
    else:
        if a>b:
            return a
        else:
            return b

print(lesserevennum(8,10))
print(lesserevennum(8,4))
print(lesserevennum(9,4))
print(lesserevennum(9,11))
print(lesserevennum(5,5))
print(lesserevennum(4,4))


def lesserevennum1(a,b):
    '''this function return the lesser of two given numbers if both numbers are even, but return the greater if one or both numbers are odd'''
    if a%2==0 and b%2==0:
        return min(a,b)
    else:
        return max(a,b)


print(lesserevennum1(8,10))
print(lesserevennum1(8,4))
print(lesserevennum(9,4))
print(lesserevennum1(9,11))
print(lesserevennum1(5,5))
print(lesserevennum1(4,4))


#ANIMAL CRACKERS


def animalcrackers(str):
    '''This function takes two word string and return True if both words begin with same letter'''
    str = str.split()
    
    firstword = str[0]
    secondword =str[1]

    return firstword[0] == secondword[0]
   

print(animalcrackers('abcd axyz'))
print(animalcrackers('abcd xxyz'))
        
    

# Python program to illustrate functions
# can be treated as objects
def shout(text):
    return text.upper()
 
print(shout('Hello'))
 
yell = shout
 
print(yell('Hello'))


# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def whisper(text):
	return text.lower()

def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function passed as an argument.""")
	print (greeting)

greet(shout)
greet(whisper)


# Python program to illustrate functions
# Functions can return another function
 
def create_adder(x):
    def adder(y):
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))

#One Way
def animal_crackers(text):
    wordlist= text.split()
    print(wordlist)

    first = wordlist[0]
    second = wordlist[1]
    return first[0] == second[0]


print(animal_crackers("Levelheaded Lama"))
print(animal_crackers("Levelheaded lama"))
print(animal_crackers("Levelheaded ama"))

#Second Way
def animal_crackers(text):
    wordlist= text.split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]
    

print(animal_crackers("Levelheaded Lama"))
print(animal_crackers("Levelheaded lama"))
print(animal_crackers("Levelheaded ama"))


#Third Way
def animal_crackers(text):
    wordlist= text.lower().split()
    #or wordlist= text.upper().split()
    print(wordlist)
    return wordlist[0][0] == wordlist[1][0]
    
print(animal_crackers("Levelheaded lama"))

#Find if any number is 20 or sum is 20

def isTwenty(a,b):
    if a+b==20:
        return True
    elif a==20:
        return True
    elif b==20:
        return True
    else:
        return False

print('\n')
print(isTwenty(8,12))
print(isTwenty(8,20))
print(isTwenty(8,2))

# OR

def isTwenty(a,b):
    return a+b==20 or a==20 or b==20
        
print('\n')
print(isTwenty(8,12))
print(isTwenty(8,20))
print(isTwenty(5,15))
print(isTwenty(6.1,13.9))
print(isTwenty(-10,30))
print(isTwenty(40/10,15+1))






