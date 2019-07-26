//Might want to change the name of this class later because its confusing.


#include <iostream>
#include "MasterDeck.h"




class Gambler {

protected:


	int num_soft_aces_in_hand;

	std::vector<card> hand;
	//Might not use this.
	std::vector<card> visible_cards;


public:


	virtual int play() = 0;
	virtual card draw_card() = 0;


	void reset() {
		hand.clear();
		visible_cards.clear();
		num_soft_aces_in_hand = 0;

	}

};



void setup_new_game(std::vector<Gambler> g) {
	
	//Distribute first card
	for (int i=0; i<g.size(); i++) {
		g[i].draw_card();
		
	}

	//Distribute second card
	for (int i=0; i<g.size(); i++) {
		g[i].draw_card();
		
	}

}




