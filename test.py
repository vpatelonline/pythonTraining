print("TEST ONLY")
print("This is test only")

print('\nIF, ELIF, ELSE')

loc = 'BANK'

if loc == 'BANK':
    print('I am in a bank')
elif loc == 'SHOP':
    print('I am in a shop')
else:
    print("I dont know where I am?")

print('\nFOR LOOP - PRINT LIST')

my_list = [1,2,3,4,5,6,7,8,9,10]

for item_in_list in my_list:
    print(item_in_list)

print('\nFOR LOOP - PRINT EVEN ODD')

for item_in_list in my_list:
    if item_in_list%2 == 0:
        print(f'{item_in_list} is an even Number:')
    else:
        print(f'{item_in_list} is an odd number')

print('\nFOR LOOP - PRINT SUM')

list_sum=0

for item_in_list in my_list:
    list_sum = list_sum + item_in_list
    print(list_sum)

print('\nFOR LOOP - PRINT TOTAL SUM')

list_sum=0
for item_in_list in my_list:
    list_sum = list_sum + item_in_list
print(list_sum)

print('\nFOR LOOP - PRINT CHARACTERS')

for char in 'Hello, How are you?':
    print(char)

my_string ='HELLO'
for char in my_string:
    print(char)

for _ in 'thanks?':
    print('Hi')

print('\nFOR LOOP - PRINT TUPLE VALUE')

tup = (1,2,3,4,5)

for item_in_tup in tup:
    print(item_in_tup)

print('\nFOR LOOP - PRINT TUPLE VALUE IN LIST')

my_list = [(1,2),(3,4),(5,6)]
for item_in_list in my_list:
    print(item_in_list)

for (a,b) in my_list:
    print(a)
    print(b)

print("\nLIST OF TUPLE")
my_list = [(1,2,3),(3,4,6),(7,8,9)]
for a,b,c in my_list:
    print(c)

print("\nDICTIONARY")
d={'K1':1, 'K2':2, 'K3':3}
for item in d:
    print(item)

for item in d.items():
    print(item)

for key,value in d.items():
    print(value)

print('\nWHILE LOOP')

X=0
while X<5:
    print(f'The value of X is {X}')
    X +=1
else:
    print('X is less than 10')

print('\nPASS')
x = [1,2,3]
for item in x:
    pass
print('end of my loop')

print('\nCONTINUE')
my_string = 'abcd'
for letter in my_string:
    if letter == 'a':
        continue
    print(letter)

print('\nBREAK')
my_string = 'abcd'
for letter in my_string:
    if letter == 'c':
        break
    print(letter)

y=0
while y<5:

    if y==2:
        break
    print(y)
    y+= 1

print('\nRANGE()')

for num in range(10):
    print(num)

for num in range(5, 10):
    print(num)

for num in range(0, 10,2):
    print(num)
   
print(list(range(0,10,2)))

index_count = 0
for letter in 'word':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count+=1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count+=1

print('\nenumerate()')

word = 'abcde'
for item in enumerate(word):
    print(item)

word = 'abcde'
for index,item in enumerate(word):
    print(index)
    print(item)
    print('\n')


sentence = "I love python language"
index = 0
print (sentence[::-1])

for index,word in enumerate(sentence):
    print('At index {} character is {}'.format(index, word))
    index+=1
    
print('\nZIP()')

list1 = [1,2,3]
list2 = ['a','b','c']
list3 = ['@','#','$']

for item in zip(list1,list2,list3):
    print(item)

for x,y,z in zip(list1,list2,list3):
    print(z)

print (list(zip(list1,list2,list3)))

print('\nUSE OF IN')

print('x' in [1,2,3])
print('x' in ['x','y'])
print('i' in ['abcdefghijklmnop','i'])

print ('mykey' in {'mykey':'abcd'})

d = {'mykey':'abcd'}
print('abc' in d.values())
print('abc' in d.keys())
print('mykey' in d.keys())

print('\nMIN() and MAX()')
mylistx = [10,20,50,3990]
print(min(mylistx))
print(max(mylistx))

print('\nFROM , IMPORT - shuffle()')

from random import shuffle
mylisty = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylisty)
print(mylisty)

randomlist = shuffle(mylisty)
print(type(randomlist))

print('\nFROM , IMPORT - RANDINT()')

from random import randint
print(randint(0,999))
print(randint(-900,-890))
mynum = randint(0,999)
print(mynum)


print('\nINPUT()')
#result = int(input('Enter a number here:'))
#print (result)
#print (type(result))
#print (float(result))

print('\nAPPEND()')

mystring = 'hello'

mylist = []
for letter in mystring:
    mylist.append(letter)
print (mylist)

print('\nLIST COMPREHENSION')
mylist = [letter for letter in mystring]
print (mylist)

mylist = [letter for letter in 'Data Science']
print (mylist)

mylist = [x for x in range(0,10)]
print (mylist)

mylist = [x**2 for x in range(0,10)]
print (mylist)

mylist = [x**2 for x in range(0,10) if x%2==0]
print (mylist)

mylist = [x**2 for x in range(0,10) if x%2!=0]
print (mylist)


F=[-32,-20,-15,-10,0,10,20,31,40,50,100,32]
C=[((temp-32)*5/9) for temp in F]
print(C)

C=[]
for temp in F:
    C.append((temp-32)*5/9)
    
print(C)

a=[]
for num in range(0,10):
    a.append(num)
    print(a)
    num+=1

print(a)


print('\nLIST COMPREHENSION - If, ELSE')

result = [x if x%2==0 else 'ODD' for x in range(0,10)]
print(result)


print('\nNESTED FOR LOOP')
mylist=[]
for x in [2,4,6]:
    for y in [10,20,30]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2,4,6] for y in [10,20,30]]
print(mylist)

print("\nUse for, .split(), and if to create a Statement that will print out list of words that start with 's':")
st = 'SAM Print only the words that start with s in this sentence'
listwiths=[]
for temp in st.split():
    if temp[0]=='s':  #to include SAM use temp[0].lower()
        listwiths.append(temp)

print(listwiths)

print('\nUse range() to print all the even numbers from 0 to 10.')

print(list(range(0,11,2)))

for x in range(0,11):
    if x%2==0:
        print(x)

for num in range(0,11,2):
    print(num)

print('\nUse a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.')

print ([x for x in range(1,51) if x%3==0])

print('\nGo through the string below and if the length of a word is even print "even!"')
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word)%2==0:
        print(word + ' is even')

print('Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".')

for x in range(1,101):

    if x%3==0 and x%5==0:
        print('FizzBuzz')
    elif x%3==0:
        print('Fizz')   
    elif x%5==0:
        print('Buzz')
    else:
        print(x)

print('\nUse List Comprehension to create a list of the first letters of every word in the string below:')

st = 'Create a list of the first letters of every word in this string'
print([word[0] for word in st.split()])

































