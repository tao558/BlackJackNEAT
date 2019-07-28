#from Player import Player
from Dealer import Dealer
from MasterDeck import MasterDeck
from Card import CardEnum, Card
import sys



#TODO: list of visible cards?
#TODO: getting error that reading cards not visible to other players...
#..... temporarily fixed it by changing second card to visible when Dealer.playing (this might be a permanent fix)
#TODO: dealer BJ and bust counts are off very slightly. Even after running 10^7 games





# Makes all of the gamblers draw 
# their first two cards
# TODO: Does a deck get restocked with a brand new deck every time?
# TODO: worried about players having their cards, then deck gets restocked, then there are more of the cards the playes have in their hand than any other card
def setup_new_game(gamblers):

    # Draw the first card
    for i in range(len(gamblers)):
        # Everyone gets a faceup card
        gamblers[i].draw_card(True)

    # Draw the second card
    for i in range(len(gamblers)):
        
        # If this is the dealer, deal card facedown
        if (isinstance(gamblers[i], Dealer)):
            gamblers[i].draw_card(False)

        # Otherwise, faceup
        else:
            gamblers[i].draw_card(True)

        
    # NOTE: The above could be done in one loop,
    # but I wrote it this way to keep the tradition
    # of how casinos deal cards




# Resets all of the gambler's states.
def reset_all_gamblers(gamblers):
    for i in range(len(gamblers)):
        gamblers[i].reset()





if __name__ == "__main__":



    num_decks = sys.argv[1]
    if (not num_decks.isdigit()):
        sys.exit("num_decks must be a positive integer")

    num_decks = int(num_decks)


    num_games_stop = sys.argv[2]
    if (not num_games_stop.isdigit()):
        sys.exit("num_games_stop must be a positive integer")
        
    num_games_stop = int(num_games_stop)



    m = MasterDeck(num_decks)
    dealer = Dealer(m)
    gamblers = [dealer]

    num_dealer_blackjacks = 0
    num_dealer_busts = 0


    for game_num in range(num_games_stop):
        setup_new_game(gamblers)
        dealer_score = dealer.play()
        reset_all_gamblers(gamblers)

        #print("Game {:d}: dealer score was {:d}".format(game_num + 1, dealer_score))

        if (dealer_score == CardEnum.BLACKJACK.value):
            num_dealer_blackjacks+=1

        if (dealer_score > CardEnum.BLACKJACK.value):
            num_dealer_busts+=1

        
    print("percent_dealer_blackjacks: {:f}".format(num_dealer_blackjacks/num_games_stop))
    print("percent_dealer_busts: {:f}".format(num_dealer_busts/num_games_stop))






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