#from Player import Player
from Dealer import Dealer
from MasterDeck import MasterDeck
from Card import CardEnum, Card
from NodeGene import NodeGene, NodeGeneTypesEnum
from ConnectionGene import ConnectionGene
from Genome import Genome
from Generation import Generation
import sys



#TODO: .... figure out return statement. Not sure if I want to have each Genome store the generation it is and vice versa or just have Generation store the genomes.

#TODO: list of visible cards?
#TODO: Make sure consistently using or not using getters and setters 



# This makes the amount of each node type specificed,
# then returns a list 
# Make sure n_in > 0 and n_out > 0
def make_node_list(n_in, n_hid, n_out):
    INPUT = NodeGeneTypesEnum.INPUT.value
    HIDDEN = NodeGeneTypesEnum.HIDDEN.value
    OUTPUT = NodeGeneTypesEnum.OUTPUT.value

    # List comp for input nodes
    inputs = [NodeGene(id, INPUT) for id in range(n_in)]
    hiddens = [NodeGene(id, HIDDEN) for id in range(n_in, n_in + n_hid)]
    outputs = [NodeGene(id, OUTPUT) for id in range(n_in + n_hid, n_in + n_hid + n_out)]

    # Now accumulate them all
    res = inputs + hiddens + outputs
    return res

    



# Makes all of the gamblers draw 
# their first two cards
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

    inno_num = 0

    # num_decks = sys.argv[1]
    # assert num_decks.isdigit(), "ERROR: num_decks must be a positive integer"

    # num_decks = int(num_decks)


    # num_games_stop = sys.argv[2]
    # assert num_games_stop.isdigit(), "ERROR: num_games_stop must be a positive integer"
        
    # num_games_stop = int(num_games_stop)



    # m = MasterDeck(num_decks)
    # dealer = Dealer(m)
    # gamblers = [dealer]

    # num_dealer_blackjacks = 0
    # num_dealer_busts = 0


    # for game_num in range(num_games_stop):
    #     setup_new_game(gamblers)
    #     dealer_score = dealer.play()
    #     reset_all_gamblers(gamblers)


    #     if (m.need_to_restock):
    #         m.stock()

    #     if (dealer_score == CardEnum.BLACKJACK.value):
    #         num_dealer_blackjacks+=1

    #     if (dealer_score > CardEnum.BLACKJACK.value):
    #         num_dealer_busts+=1

        
    # print("percent_dealer_blackjacks: {:f}".format(num_dealer_blackjacks/num_games_stop))
    # print("percent_dealer_busts: {:f}".format(num_dealer_busts/num_games_stop))




    # Lets make a rudimentary Genome for testing.
    node_list = make_node_list(2, 1, 1)
    g = Genome(node_list, [])

    print("Before adding connection")
    g.print_nodes()
    g.print_connections()

    inno_num = g.mutate_add_connection(inno_num)

    print("After adding connection")
    g.print_connections()
    g.print_nodes()


    print("About to add node")

    inno_num = g.mutate_add_node(inno_num)

    print("After adding node")
    g.print_connections()
    g.print_nodes()

    
    

    




