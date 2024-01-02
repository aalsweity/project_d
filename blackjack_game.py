import random

class Blackjack:
    def __init__(self, dealer, player):
        self.deck = self.shuffle_deck()
        self.dealer = dealer
        self.player = player
        self.turn = player
        
    def shuffle_deck(self):
        card_suits = {"Clubs", "Diamonds","Hearts","Spades"}
        card_set = {2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"}
        # make function to create cards from card_suits and card_set
        return deck # deck is not ready yet.
        
    def begin_game(self):
        #betting function goes here
        if len(self.deck) < 10:
            print("We're low on cards. Gotta Shuffle.")
            self.deck = self.shuffle_deck()
        #deal cards starts here
        self.turn = self.player
        
        if self.player.blackjack(): #incomplete blackjack function. Put here temporarily.
            print(f"The player got a Blackjack! The player wins $ {self.player.bet * 2:.2f }")
        #money and betting still incomplete.
        elif self.player.total > 21:
            print(f"The player has busted. You lost ${self.player.bet}")
            self.player.money -= self.player.bet
        
        elif self.dealer.total > 21:
            print(f"The dealer has busted. You win {self.player.bet}")
            self.player.money += self.player.bet
            
        elif self.player.total > self.dealer.total:
            print(f"The player wins. You win ${self.player.bet}")
            self.player.money += self.player.bet
        
        elif self.player.total < self.dealer.total:
            print(f"the dealer wins. You lost ${self.player.bet}")
            self.player.money -= self.player.bet
        
        else:
            print("The player and the dealer tied. It's a Draw.")
        self.show_cards()
        print(f"You currently have ${self.player.money}")
    
    
    def show_cards(self):
        if self.turn == self.player:
            player_cards = ""
            for card in self.player.cards:
                player_cards += f"{card}"
            print(f"Player's hand: {player_cards{:-2}} ----- {self.player.total}") # total function not ready. Temp.
            print(f"Dealer's hand: {self.dealer.cards[0]} Face Down Card")
            
        else:
            player_cards = ""
            for card in self.player.cards:
                player_cards += f"{card}"
            print(f"Player's hand: {player_cards{:-2}} ----- {self.player.total}")
            dealers_cards = ""
            for card in self.dealer.cards:
                dealers_cards += f"{card}"
            print(f"Dealer's hand: {dealers_cards{:-2}} ----- {self.dealer.total}") 
        
    def card(self,card_suits, card_set):
        
        
# Just realized I was supposed to be making classes and their functions. Not put it all in one class. SMH.