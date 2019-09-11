from NodeGene import NodeGene, NodeGeneTypesEnum
from ConnectionGene import ConnectionGene
from Genome import Genome
from Generation import Generation
import sys


#MASTER TODOLIST:
#TODO: fully implement bias nodes
#TODO: nodes keep list of incoming and outgoing connections?
#TODO: should crossover return an inno num?




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
    pass




if __name__ == "__main__":
    c1 = sys.argv[1]
    c2 = sys.argv[2]
    c3 = sys.argv[3]
    

    
    

    




