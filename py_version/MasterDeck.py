from Card import *
from random import shuffle

#TODO: See if there is a better way around importing. Might not be as bad as I thought if just keep implementing 




class DeckParameters(Enum):
    NUM_TENS_PER_DECK = 16
    NUM_OTHER_CARDS_PER_DECK = 4
    NUM_CARDS_PER_STANDARD_DECK = 52







class MasterDeck:
	


    def __init__(self, num_std_decks_t):
        self.num_std_decks = num_std_decks_t
        self.deck = list()
        self.stock()


    def stock(self):
        # Add each in each card
        for card_value in range(CardEnum.TWO.value, CardEnum.HIGH_ACE.value):
            if (card_value == CardEnum.TEN.value):
                self.deck.extend( [Card(card_value, False) for i in range( DeckParameters.NUM_TENS_PER_DECK.value )] )

            else: 
                self.deck.extend( [Card(card_value, False) for i in range( DeckParameters.NUM_OTHER_CARDS_PER_DECK.value )] )

        
        # Randomize the deck
        shuffle(self.deck)


    def give_card(self):
        ret = self.deck.pop()
        if (len(self.deck) == 0):
            self.stock()

        return ret






