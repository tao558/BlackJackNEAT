#include "Gambler.h"





class Dealer: virtual public Gambler {


private:

	MasterDeck m;




public:


	//TODO: Do player and dealer really need to inherit from gambler? If not, get rid of reference here and fix classes accordingly.
			//It just seems weird to have the player be able to see the card. Maybe just make the gambler class only have player()? Need to figure out
				//Class structure before proceeding
	Dealer(MasterDeck m_t) {
		m = m_t;
	}



	//Need to figure out how to deal with case where either or both of the first two
	//drawn cards sssare aces. Then need to implement the play(int) function
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
