import sys



class Card:
    def __init__(self, value_t, is_visible_t):
        self.value = value_t
        self.is_visible = is_visible_t



    def is_faceup(self):
        return self.is_visible


    def get_value(self):
        try:
            if (self.is_faceup()):
                return self.value

            raise RuntimeError("ERROR: Tried to look at a card that isn't visible to any gamblers")
        except RuntimeError as e:
            print(e)
            sys.exit()



from enum import Enum
class CardEnum(Enum):
    LOW_ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    HIGH_ACE = 11
    BLACKJACK = 21


