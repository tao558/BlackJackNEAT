#include <iostream>
#include <cstdlib>


class Card {

    private:

        card_val val;
        bool visible;



    public:

        Card(card_val val_t, bool visible_t) {
            val = val_t;
            visible = visible_t;
        }


        bool is_faceup() {
            return visible;
        }


        card_val get_val() {
            try {
                if (this -> visible)
                    return val; 

                throw 21;
            }
            catch (int e){
	        	std::cout << "Tried to look at a card that shouldn't be visible to other players" << std::endl;
		        exit(EXIT_FAILURE);
	        }
 
            
        }

};




enum card_val {
    LOW_ACE = 1,
	TWO = 2,
	THREE = 3,
	FOUR = 4,
	FIVE = 5,
	SIX = 6,
	SEVEN = 7,
	EIGHT = 8,
	NINE = 9,
	TEN = 10,
	HIGH_ACE = 11,
	BLACKJACK = 21
};

