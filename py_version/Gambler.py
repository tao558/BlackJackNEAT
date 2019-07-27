from Card import Card, CardEnum


#TODO: might want to change the name of this class later because its confusing.


class Gambler:
	def __init__(self, master_deck_t):
		self.num_soft_aces = 0
		self.hand = list()
		self.master_deck = master_deck_t  # This is a reference


	# Resets the gambler for another round
	def reset(self):
		self.num_soft_aces = 0
		self.hand.clear()



	def draw_card(self):
		next_card = self.master_deck.give_card()
		self.hand.append(next_card)
		
		if (next_card.value == CardEnum.HIGH_ACE):
			self.num_soft_aces += 1

		return next_card










# void setup_new_game(std::vector<Gambler> g) {
	
# 	//Distribute first card
# 	for (int i=0; i<g.size(); i++) {
# 		g[i].draw_card();
		
# 	}

# 	//Distribute second card
# 	for (int i=0; i<g.size(); i++) {
# 		g[i].draw_card();
		
# 	}

# }




