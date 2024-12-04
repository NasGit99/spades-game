from create_deck import *

def play_spades():

    player_game = create_players()
    
    team_1 = 0
    team_2 = 0

    current_pile =[]
    current_suit = set()

    turn = 0
    rounds = 0

    rank_values = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "jack": 11, "queen": 12, "king": 13, "ace": 14
}

    while team_1 or team_2 < 300:
        while True:

            # Picks the players in order, later iterations will pick the deck based on the winner

            for player in player_game[turn]:
                print(f'{player.name},  is playing')

                # Grabs their deck and list out the index to select

                for i, card in enumerate(player.deck):
                    print(f'Option {i}, card is {card}\n')
                
                card_select =  int(input('From the cards above pick one to select: '))
                
                #Validation for card to be in deck

                if card_select < 0 or card_select >= len(player.deck):
                    print("Invalid selection. Try again.")
                    continue

                selected_suit = player.deck[card_select].split()[0].lower()

                # Check if the current suit exists, need to fix validation since it still allows users to bypass suit
                if current_suit:
                    if selected_suit not in current_suit:
                        print(f"Card suit '{selected_suit}' does not match the current suit: {current_suit}")
                        continue  # Stay in the loop for another selection

                if not current_suit:
                    current_suit.add(player.deck[card_select].split()[0])
                   

                #Appends the card selected to current pile

                current_pile.append(player.deck[card_select])
                
                #Removes card from players hand

                player.deck.pop(card_select)

                
                #Displays current pile

                print(len(player.deck))
                print(current_pile)
                print(current_suit)


            turn += 1


            if turn == 4:  # All 4 players have played
                rank_cards = [
                    rank_values.get(card.split()[1].lower(), 0) for card in current_pile
                ]
                print(rank_cards)
                highest_card = current_pile[rank_cards.index(max(rank_cards))]
                print(f"Highest card: {highest_card}")

                current_pile = []  # Clear pile for the next round
                current_suit.clear()  # Clear current suit

                turn = 0
                break

        team_1_books = 0
        team_2_books = 0

play_spades()