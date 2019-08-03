
from Gambler import Gambler
from Card import Card, CardEnum


#Inheritance: https://www.geeksforgeeks.org/inheritance-in-python/

class Dealer( Gambler ): 

	def __init__(self, master_deck_t):
		Gambler.__init__(self, master_deck_t)




	def play(self):
		# Make all cards visible
		self.hand[0].set_visibility(True)
		self.hand[1].set_visibility(True)

		score = self.hand[0].get_value() + self.hand[1].get_value()


 		# These are the conditions that the dealer hits on.
		# TODO: Add splits
		# TODO: test the while() condition and while() body
		while ( (score < 17 and self.num_soft_aces == 0) or (score <= 17 and self.num_soft_aces > 0) or (score > 21 and self.num_soft_aces > 0) ):
			# If we've busted but we have soft aces, fix that
			if (score > CardEnum.BLACKJACK.value and self.num_soft_aces > 0):
				self.num_soft_aces-=1
				score -= (CardEnum.HIGH_ACE.value - CardEnum.LOW_ACE.value)
			
			
			# Otherwise, draw another card!
			else:
				next_card = Gambler.draw_card(self, True)   #TODO: CHECK THIS WHEN YOU HAVE INTERNET
				score += next_card.get_value()
				if (next_card == CardEnum.HIGH_ACE.value):
					self.num_soft_aces+=1

		
		return score











