
from Gambler import *


#Inheritance: https://www.geeksforgeeks.org/inheritance-in-python/

class Dealer( Gambler ): 

	def __init__(self, master_deck_t):
		pass




	def play(self):
		score = self.hand[0].get_value() + self.hand[1].get_value()

 		# These are the conditions that the dealer hits on.
		# TODO: Add splits
		# TODO: test the while() condition and while() body
		while( (score < 17 & self.num_soft_aces == 0) | (score <= 17 & self.num_soft_aces > 0) | (score > 21 & self.num_soft_aces > 0) ):
			
			# If we've busted but we have soft aces, fix that
			if (score > 21 & self.num_soft_aces > 0):
				self.num_soft_aces-=1
				score -= (CardEnum.HIGH_ACE - CardEnum.LOW_ACE)
			
			
			# Otherwise, draw another card!
			else:
				next_card = Gambler.draw_card(self)   #TODO: CHECK THIS WHEN YOU HAVE INTERNET
				score += next_card.get_value()
				if (next_card == CardEnum.HIGH_ACE.value):
					self.num_soft_aces+=1

		
		return score











