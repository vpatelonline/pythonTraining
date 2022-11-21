
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
        
    




