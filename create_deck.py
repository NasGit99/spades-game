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


    



