#include "enums.h"
#include <algorithm>
#include <vector>


typedef int card;

class MasterDeck {

private:

	int num_std_decks;
	int num_cards_left;
	std::vector<card> master_deck;



	void stock_deck() {
		for (int i=LOWEST_CARD; i<=ACE; i++){
			if (i == 10) 
				master_deck.insert(master_deck.end(), num_std_decks * NUM_TENS_PER_DECK, i);

			else
				master_deck.insert(master_deck.end(), num_std_decks * NUM_OTHER_CARDS_PER_DECK, i);

		}

		//Now shuffle deck
		std::random_shuffle(master_deck.begin(), master_deck.end());
		num_cards_left = master_deck.size();
	}


public:

	MasterDeck(int num_std_decks_t) {
		num_std_decks = num_std_decks_t;
		stock_deck();

	}



	card give_card() {
		int ret = master_deck[num_cards_left - 1];
		master_deck.pop_back();
		num_cards_left--;
		if (num_cards_left == 0) {
			stock_deck();
		}

		return ret;
	}






};