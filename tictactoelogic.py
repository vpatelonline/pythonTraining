''''
def user_choice():

    #VARIABLES
    #INITIAL  
    choice = 'WRONG'
    acceptable_range = range(0,10)
    within_range = False
    
    #Two CONDITIONS TO CHECK
    while choice.isdigit()==False or within_range==False:
        choice=input("Please enter number between 0-10: ")

        #DIGIT CHECK
        if choice.isdigit()==False:
            print("Sorry, Please enter digit only")

        #RABGE CHECK
        if choice.isdigit()==True:   #if choice.isdigit()  is also same
            if int(choice) in acceptable_range:
                within_range=True
            else:
                print("Sorry, This is out of range number between 0-10")
                within_range=False


user_choice()

'''



game_list=[0,1,2]

def display_game(game_list):
    print("Here is the current list:")
    print(game_list)

display_game(game_list)

def position_choice():
    choice='wrong'

    while choice not in ['0','1','2']:
        choice=input("Pick a position (0,1,2):")
        if choice not in ['0','1','2']:
            print("Sorry, Invalid choice")
    
    return int(choice)

position_choice()


def replacement_choice(game_list,position):
    user_placement=input("Type a string to  place at position:")
    game_list[position] = user_placement
    return game_list

def gameon_choice():
    choice='wrong'
    while choice not in ['Y','N']:
        choice=input("Keep Playing? (Y or N)):")
        if choice not in ['Y','N']:
            print("Sorry, Invalid choice, Please select Y or N")
    
    if choice=="Y":
        return True
    else:
        return False


game_on=True
game_list=[0,1,2]

while game_on:
    display_game(game_list)
    position =position_choice()
    game_list=replacement_choice(game_list,position)
    display_game(game_list)

    game_on=gameon_choice()