#Compute vloume

def vol(radius):
    return (4/3)*(3.14)*(radius**3)

print(f"{vol(2)}\n")


# Is given number in range using if else?

def range_check_1(num,low,high):

    if num>low and num<high:
        print(f'{num} Number is in range between {low} and {high}')
    else:
        print('Number is not in range')

range_check_1(5,2,7)

# Is given number in range using range()?
def range_check_2(num,low,high):
    print(f'{num} is in range between {low} and {high}?', num in range(low, high+1))

range_check_2(8,2,7)

#Count uppercase and lower latters - Using for, if , else

my_string='Hello Mr. Rogers, how are you this fine Tuesday?'
def up_low(s):
    lowecase=0
    uppercase=0
    for char in s:
        if char.isupper():
            uppercase+=1
        elif char.islower():
            lowecase+=1
        else:
            pass

    print(f"\nOriginal string:{s}")
    print(f"Total upper case latters are: {uppercase}")
    print(f"Total lower case latters are: {lowecase}")

up_low(my_string)

#Count uppercase and lower latters - Using dict

def up_low_dict(s):
    d={'upper':0,'lower':0}
    for char in s:
        if char.isupper():
           d['upper'] += 1
        elif char.islower():
            d['lower'] += 1
        else:
            pass

    print(f"\nOriginal string:{s}")
    print(f"Total upper case latters are: {d['upper']}")
    print(f"Total lower case latters are: {d['lower']}")

up_low_dict(my_string)


#list unique number

my_list=[1,2,3,4,2,3,4,1,1,3,3]
#print(list(set(my_list)))

def unique_list(lst):
    seen_number=[]
    for number in lst:
        if number not in seen_number:
            seen_number.append(number)
    return seen_number

print(unique_list(my_list))


#palindrome - Check if string is equal to reverse

def palindrome(s):
    #Remove space
    s=s.replace(' ','')
    #Check if string is equal to reverse
    return(s == s[::-1])
    

print(palindrome('n ur ses r un'))
print(palindrome('nurses run'))



#Is pangram - Words or sentence containing  every  latter of the alphabet at least one?

import string

def isPangram(str1, alpahabet=string.ascii_lowercase):

    #Create a set of alphabet
    alphaset=set(alpahabet)

    #Remove space
    str1=str1.replace(' ','')

    #Convert into all lower case
    str1=str1.lower()

    #Grab all unique letter from string
    str1=set(str1)

    #Alphabet set == string set

    return str1==alphaset

print(isPangram("The quick brown fox jumps over the lazy dog"))


#Anagrams
def is_anagram(s1,s2):

    if (sorted(s1)==sorted(s2)):
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")

is_anagram('lissten', 'silent')



print('\n')


mylist=[1,2,3]

mylist.append(4)
print(mylist)

mylist.pop()
print(mylist)

mylist.clear()
print(mylist)

mylist1=[5,6,7,8,6]
print(mylist1)
mylist2 = mylist1.copy()
print(mylist2)

print(mylist2.count(6))

mylist3 = ['a','b','c','d','e']
print(mylist3.index('d'))

mylist3.insert (4,'A')
print(mylist3)

mylist3.pop()
print(mylist3)

mylist3.remove('b')
print(mylist3)

mylist3.reverse()
print(mylist3)

mylist3.sort()
print(mylist3)

