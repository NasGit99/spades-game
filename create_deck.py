import random
class Card:
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number

    def create_suits():
        

        hearts = [Card('hearts', number) for number in range(2, 11)]
        spades = [Card('spades', number) for number in range(2, 11)]
        clubs = [Card('clubs', number) for number in range(2, 11)]
        diamonds =[Card('diamonds', number) for number in range(2, 11)]

        all_suits = [hearts,spades,clubs,diamonds]
        
        return all_suits

    def create_deck():
        
        deck =[]
        
        
        extra_cards = ['joker', 'queen', 'king', 'ace']
        
        
        suits = Card.create_suits()
        for suit in suits:
            for card in suit:
                deck.append(card.suit + ' ' + str(card.number)) 
            
            for cards in extra_cards:
                deck.append(card.suit+ ' '+ str(cards))
        
        random.shuffle(deck)

        return deck
        

class player:
    def __init__ (self,name,deck):
        self.name = name
        self.deck = deck

def create_players():
    
    finalized_deck = Card.create_deck()

    p1 = player('p1', sorted(finalized_deck[:13]))
    p2 = player('p2',sorted(finalized_deck[13:26]))
    p3 = player('p3',sorted(finalized_deck[26:39]))
    p4 = player('p4',sorted(finalized_deck[39:52]))

    player_list = [[p1,p2,p3,p4]]

    print('Players Created\n')

    return player_list


def play_spades():

    player_game = create_players()
    
    team_1 = 0
    team_2 = 0

    #while team_1 or team_2 < 300:


    current_pile =[]

    turn = 0
    rounds = 0

    while rounds < 14:
        while turn <4:
            #picks the players in order
            for player in player_game[turn]:
                print(f'{player.name},  is playing')
                #Grabs their deck and list out the index
                for i, card in enumerate(player.deck):
                    print(f'Index is {i}, card is {card}\n')

                card_select =  int(input('From the cards above pick one to select: '))

                current_pile.append(card_select)

            #Need to remove a card from players hand based on the index. player_game[turn].deck.pop(insert index here)
                player.deck.pop(card_select)

                print(len(player.deck))


            turn +=1
            #Determine the winner here, also need a function that determines winners of face cards

    turn -3


        #If the highest value is either index 0 or 2 or index 1 or 3  then give a point for that team
            
    rounds +=1

    team_1_books = 0
    team_2_books = 0

play_spades()

    



