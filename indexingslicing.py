# Convert first and fourth Chars in capital

#Using indexing and slicing
def convertchars(name):
    first=name[0].upper()
    inbetween=name[1:3]
    fourth=name[3].upper()
    rest=name[4:]
    return first+inbetween+fourth+rest

print(convertchars('macdonald'))

#Using capitalize()
def convertchars(name):
    first_half=name[:3]
    second_half=name[3:]
    return first_half.capitalize()+second_half.capitalize()

print(convertchars('macdonald'))


#Reverse

def reversestring(text):
    wordlist = text.split()
    rever = wordlist[::-1]
    return ' '.join(rever)

print(reversestring('How are you?'))

#abs -absolute
x= abs(100-104)<=10
print (x)

def summer_69(arr):
    total=0
    add=True

    for num in arr:
        while add:
            if num!=6:
                total+=num
                break
            else:
                add=False

        while not add:
            if num!=9:
                break
            else:
                add =True
                break
    return total

#summer_69([1,3,5])
#print(summer_69([4,5,9,7,8,6]))
print(summer_69([2,1,6,9,11]))




