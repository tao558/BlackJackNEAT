#include <map>
#include <cstdlib>


class MasterDeck{
private:
	std::map<int, int> deck;
	const int num_std_decks;
	const int ACE = 11;
	const int NUM_TENS_PER_DECK = 16;
	const int NUM_OTHER_CARDS_PER_DECK = 4;
	const int NUM_CARDS_PER_STANDARD_DECK = 52;



	int num_cards_remaining;



	void stock(){
		num_cards_remaining = NUM_CARDS_PER_STANDARD_DECK * num_std_decks;

		for(int card_val=2; card_val<=ACE; card_val++){
			if (card_val == 10)
				deck.insert( std::pair<int, int>(card_val, NUM_TENS_PER_DECK * num_std_decks) );
			
			else
				deck.insert( std::pair<int, int>(card_val, NUM_OTHER_CARDS_PER_DECK * num_std_decks) );
		}
	}


	//Next time, finish draw function. 


public:
	
	MasterDeck(int num_std_decks_t): num_std_decks(num_std_decks_t) {
		stock();
		
	}


	int drawCard(){
		//Draw a card, then check if deck is empty. if so, clear deck, then call stock.

	}



};