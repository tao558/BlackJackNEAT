from NodeGene import *
from ConnectionGene import ConnectionGene
from Genome import Genome
from Generation import Generation
import sys


#MASTER TODOLIST:
#TODO: How to feedforward? Initialize random weights? nodes keep list of incoming and outgoing connections?
#TODO: should crossover return an inno num?




# This makes the amount of each node type specificed,
# then returns a list 
# Make sure n_in > 0 and n_out > 0
def make_node_list(n_in, n_hid, n_out):


    # List comp for input nodes
    inputs = [InputNode(id) for id in range(n_in)]
    hiddens = [HiddenNode(id) for id in range(n_in, n_in + n_hid)]
    outputs = [OutputNode(id) for id in range(n_in + n_hid, n_in + n_hid + n_out)]

    # Now accumulate them all
    res = inputs + hiddens + outputs
    return res

    



# Makes all of the gamblers draw 
# their first two cards
def setup_new_game(gamblers):
    pass




if __name__ == "__main__":
    c1 = sys.argv[1]
    c2 = sys.argv[2]
    c3 = sys.argv[3]
    

    
    

    




