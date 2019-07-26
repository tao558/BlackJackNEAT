#include "Card.h"
#include <algorithm>
#include <vector>


typedef int card;

class MasterDeck {

private:

	int num_std_decks;
	std::vector<Card> master_deck;



	void stock_deck() {
		for (int i=TWO; i<=HIGH_ACE; i++){
			if (i == 10) 
				master_deck.insert( master_deck.end(), num_std_decks * NUM_TENS_PER_DECK, Card(static_cast<card_val>(i), false) );

			else
				master_deck.insert( master_deck.end(), num_std_decks * NUM_OTHER_CARDS_PER_DECK, Card(static_cast<card_val>(i), false) );

		}

		//Now shuffle deck
		std::random_shuffle(master_deck.begin(), master_deck.end());
	}


public:

	MasterDeck(int num_std_decks_t) {
		num_std_decks = num_std_decks_t;
		stock_deck();

	}



	Card give_card() {
		Card ret = master_deck[master_deck.size() - 1];
		master_deck.pop_back();
		if (master_deck.size() == 0) {
			stock_deck();
		}

		return ret;
	}

};





enum deck_constants {
	NUM_TENS_PER_DECK = 16,
	NUM_OTHER_CARDS_PER_DECK = 4,
	NUM_CARDS_PER_STANDARD_DECK = 52,
};