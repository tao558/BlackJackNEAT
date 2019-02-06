#include "Gambler.h"





class Dealer: virtual public Gambler{



public:

	//TODO: FIX THIS????
	Dealer(MasterDeck* m_t): Gambler(m_t) {}



	//Need to figure out how to deal with case where either or both of the first two
	//drawn cards are aces. Then need to implement the play(int) function
	int play() {
		int score = first_card + second_card;
		//These are the conditions that the dealer hits on.
		while( (score < 17 && num_soft_aces_in_hand == 0) || score <= 17 && num_soft_aces_in_hand > 0 ) {
			int next_card = draw_card();
			all_cards_drawn.push_back(next_card);
			score += next_card;
			if (next_card == ACE) {
				num_soft_aces_in_hand++;
			}


			if (score > 21 && num_soft_aces_in_hand > 0) {
				num_soft_aces_in_hand--;
				score -= 10;
			}

		}

		return score;
	}



	
};