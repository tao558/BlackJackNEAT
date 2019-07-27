#from Player import Player
from Dealer import Dealer
from MasterDeck import MasterDeck


num_decks = 3
num_games_stop = 10



m = MasterDeck(num_decks)
dealer = Dealer(m)
all_players = [dealer]


# TODO: Play some games! Start off with just the dealer and make sure that the play() function works correctly. Then work on NN











#include <iostream>
#include "Dealer.h"
#include "Player.h"






# int main(int argc, char* argv[]) {
# 	int num_std_decks = atoi(argv[1]);
# 	const int num_games_stop = atoi(argv[2]);
# 	try {	
# 		if (num_std_decks <= 0)
# 			throw 21;
# 	}
# 	catch (int e){
# 		std::cout << "The number of decks is invalid" << std::endl;
# 		return 0;
# 	}

# 	srand(time(0));
# 	MasterDeck m(num_std_decks);
	
# 	Dealer d(m);
# 	int num_busts = 0;
# 	int num_blackjacks = 0;

# 	std::vector<Gambler*> all_players;
# 	all_players.push_back(&d);


# 	for (int i=0; i<num_games_stop; i++) {
# 		setup(all_players);
# 		int score = d.play();
# 		//std::cout << score << std::endl;
# 		d.reset();
		


# 		if (score > 21){
# 			num_busts++;
# 		}

# 		if (score == 21) {
# 			num_blackjacks++;
# 		}
# 	}




# 	std::cout << "percent of blackjacks: " << (float) num_blackjacks/num_games_stop << std::endl;
# 	std::cout << "percent of busts: " << (float) num_busts/num_games_stop << std::endl;

# 	return  0;
# }