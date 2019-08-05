from Card import Card, CardEnum
from random import shuffle
import sys




class MasterDeck:
    # Define some game parameters
    NUM_TENS_PER_DECK = 16
    NUM_OTHER_CARDS_PER_DECK = 4
    NUM_CARDS_PER_STANDARD_DECK = 52



    def __init__(self, num_std_decks_t):
        self.num_std_decks = num_std_decks_t
        self.deck = list()
        self.need_to_restock = False
        self.TOTAL_NUM_CARDS = self.num_std_decks * self.NUM_CARDS_PER_STANDARD_DECK 

        self.stock()   


    def stock(self):
        self.deck.clear()
        # Add each in each card. 
        # The +1 at the end of the range() call is there so Aces are included, since range() is exclusive at the upper bound
        for card_value in range(CardEnum.TWO.value, CardEnum.HIGH_ACE.value + 1):
            if (card_value == CardEnum.TEN.value):
                self.deck.extend( [Card(card_value, False) for i in range( self.NUM_TENS_PER_DECK * self.num_std_decks )] )

            else: 
                self.deck.extend( [Card(card_value, False) for i in range( self.NUM_OTHER_CARDS_PER_DECK * self.num_std_decks)] )

        
        # Randomize the deck
        shuffle(self.deck)

        assert len(self.deck) == self.TOTAL_NUM_CARDS, ('ERROR: Wrong number of cards in the deck.' 
                                                       ' Number expected: {:d}. Number in deck: {:d}').format(self.TOTAL_NUM_CARDS, len(self.deck))
        

        # No longer need to restock
        self.need_to_restock = False


    def give_card(self):
        assert len(self.deck) > 0, "ERROR: Deck has no more cards!"
        ret = self.deck.pop()
        if (len(self.deck) / self.TOTAL_NUM_CARDS < 0.2):
            self.need_to_restock = True

        return ret






