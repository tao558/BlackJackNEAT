//Might want to change the name of this class later because its confusing.


#include <iostream>
#include "MasterDeck.h"




class Gambler {

protected:
	//These will be initialized after the zeroth turn.
	card first_card;
	card second_card;    //This will be face down for the dealer.
	int num_soft_aces_in_hand;
	MasterDeck* m;


	//Might not use this.
	std::vector<card> all_cards_drawn;


public:

	Gambler(MasterDeck* m_t) {
		m = m_t;
		first_card = 0;
		second_card = 0;
	}



	card draw_card(){
		return m -> give_card();
	}

	virtual int play() = 0;


	void reset(){
		all_cards_drawn.clear();
		num_soft_aces_in_hand = 0;
		
		first_card = 0;
		second_card = 0;
	}


	void draw_first_card() {
		first_card = draw_card();
		all_cards_drawn.push_back(first_card);
		num_soft_aces_in_hand += first_card == ACE;

	}



	void draw_second_card() {
		second_card = draw_card();
		all_cards_drawn.push_back(second_card);
		num_soft_aces_in_hand += second_card == ACE;

	}


};



void setup(std::vector<Gambler*> g) {
	
	//Distribute first card
	for (int i=0; i<g.size(); i++) {
		g[i] -> draw_first_card();
		
	}

	//Distribute second card
	for (int i=0; i<g.size(); i++) {
		g[i] -> draw_second_card();
		
	}

}




