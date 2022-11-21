example = [1,2,3,4,5,6,7,8,9]
from random import shuffle
shuffle(example)
print(example)

#SHUFFLE GAME

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)
print(result)


mylist2 = ['','0','']
shuffle(mylist2)
print(mylist2)

def player_guess():
    
    guess=''

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1 or 2: ")
        
    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Correct')
    else:
        print('worng')
        print(mylist)


#INTITIAL LIST
mylist = ['','O','']
#SHUFFLE LIST
mixedup_list = shuffle_list(mylist)
#USER GUESS
guess = player_guess()
#CHECK GUESS
check_guess(mixedup_list,guess)







