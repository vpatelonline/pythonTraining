#CARD
#SUIT,RANK, VALUE
import random

suits = ('Hearts','Dimonds','Spades','Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'seven', 'Eight', 'Nine', 
            'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit

#DECK

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
            return self.all_cards.pop()

#new_deck = Deck()
#first_card = new_deck.all_cards[0]

#print(first_card)

#new_deck.shuffle()
#first_card = new_deck.all_cards[0]
#print(first_card)

#for card_object in new_deck.all_cards:

#   print(card_object)


class Player:

    def __init__(self,name):
        self.name = name
        self.all_card = []
    
    def remove_one(self):
        return self.all_card.pop(0)

    def add_cards(self, new_cards):

        if type(new_cards)==type([]):
            #List of multiple card object
            self.all_card.extend(new_cards)
        else:
            #For a single card object
            self.all_card.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_card)} cards'

#new_player=Player("Jose")
#print(new_player)

#GAME SETUP

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


#While game on
game_on = True

round_num = 0

while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_card) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break

    if len(player_two.all_card) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break

    # START A NEW ROUND
    player_one_card = []
    player_one_card.append(player_one.remove_one())

    player_two_card = []
    player_two_card.append(player_two.remove_one())



    #While at war
    at_war = True

    while at_war:

        if player_one_card[-1].value > player_two_card[-1].value:
            player_one.add_cards(player_one_card)
            player_one.add_cards(player_two_card)

            at_war=False

        elif player_one_card[-1].value < player_two_card[-1].value:
            player_two.add_cards(player_one_card)
            player_two.add_cards(player_two_card)

            at_war=False

        else:
            print('WAR!')

            if len(player_one.all_card) < 5:
                print("Player ONE unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break
            
            elif len(player_one.all_card) < 5:
                print("Player TWO unable to declare war")
                print("PLAYER ONE WINS!")
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_card.append(player_one.remove_one())
                    player_two_card.append(player_two.remove_one())


#PLAYER