import pytest
from NodeGene import NodeGene, NodeGeneTypesEnum
from ConnectionGene import ConnectionGene
from Genome import *
from Generation import Generation
import numpy as np

# TODO: would this technically be a fixture?
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

    

@pytest.fixture
def supply_generation_one_basic_genome():
    generation = Generation([])

    nodes = make_node_list(1, 0, 1)
    cons = [ ConnectionGene(nodes[0], nodes[1], np.random.uniform(), 1, 0) ]
    genome = Genome(nodes, cons, generation)
    generation.genomes.append(genome)
    return generation
    



@pytest.fixture
def supply_generation_two_basic_genomes():
    generation = Generation([])

    nodes = make_node_list(1, 1, 2)
    cons1 = [ ConnectionGene(nodes[0], nodes[1], np.random.uniform(), 1, 0),
              ConnectionGene(nodes[1], nodes[2], np.random.uniform(), 1, 1) ]
    genome1 = Genome(nodes, cons1, generation)

    cons2 = [ ConnectionGene(nodes[0], nodes[1], np.random.uniform(), 1, 0),
              ConnectionGene(nodes[2], nodes[3], np.random.uniform(), 1, 2) ]
    genome2 = Genome(nodes.copy(), cons2, generation)
    
    generation.genomes.extend([genome1, genome2])
    return generation
    


# Should add a node with ID == 2 and 
# update generation's connections_made with the 2 two connections
# and update generation's connections_split with the old connection
def test_add_node(supply_generation_one_basic_genome):
    generation = supply_generation_one_basic_genome
    genome = generation.genomes[0]

    inno_num = 0
    inno_num = genome.mutate_add_node(inno_num)
    active_cons =[con for con in genome.connections if con.enabled]
    inactive_cons = [con for con in genome.connections if not con.enabled]

    assert inno_num == 2
    assert len(active_cons) == 2
    assert len(genome.connections) == 3
    assert len(genome.nodes) == 3
    assert genome.nodes[2].id == 2
    assert genome.nodes[2].type == NodeGeneTypesEnum.HIDDEN.value

    assert genome.next_node_id == 3
    assert genome.n_input_nodes == 1
    assert genome.n_hidden_nodes == 1
    assert genome.n_output_nodes == 1

    assert active_cons[0] == ConnectionGene(NodeGene(0, None), NodeGene(2, None), None, None, None)
    assert active_cons[1] == ConnectionGene(NodeGene(2, None), NodeGene(1, None), None, None, None)
    assert inactive_cons[0] == ConnectionGene(NodeGene(0, None), NodeGene(1, None), None, None, None)



def test_add_connection_normal(supply_generation_one_basic_genome):
    generation = supply_generation_one_basic_genome
    genome = generation.genomes[0]

    # For all of the other tests, we'll use the connection in the genome...
    # in this one, we'll manually delete it, then add it back using the mutation 
    genome.connections.clear()
    inno_num = 0
    inno_num = genome.mutate_add_connection(inno_num)

    assert inno_num == 1
    assert len(genome.connections) == 1
    assert genome.connections[0].enabled
    assert genome.connections[0] == ConnectionGene(NodeGene(0, None), NodeGene(1, None), None, None, None)
    assert genome.connections[0].inno_num == 1


def test_reactivate_connection(supply_generation_one_basic_genome):
    generation = supply_generation_one_basic_genome
    genome = generation.genomes[0]

    # Manually disable the only connection, then reenable it
    genome.connections[0].enabled = False
    assert not genome.connections[0].enabled
    
    inno_num = 0
    inno_num = genome.mutate_add_connection(inno_num)

    assert len(genome.connections) == 1
    assert genome.connections[0].enabled
    assert genome.connections[0].inno_num == 0
    assert len(genome.nodes) == 2





# This shouldn't change anything since the genome is fully connected
def test_add_connection_fully_connected(supply_generation_one_basic_genome):
    generation = supply_generation_one_basic_genome
    genome = generation.genomes[0]

    inno_num = 0
    inno_num = genome.mutate_add_connection(inno_num)

    assert inno_num == 0
    assert genome.is_fully_connected()
    assert len(genome.connections) == 1
    assert len(genome.nodes) == 2


# Tests that crossing over works if one of the genomes is empty
def test_crossover_empty_genome(supply_generation_one_basic_genome):
    pass



# Tests that crossing over works in a very basic case: 
# 1 matching gene, 1 disjoint, and 1 excess
def test_crossover_basic(supply_generation_two_basic_genomes):
    generation = supply_generation_two_basic_genomes
    g1 = generation.genomes[0]
    g2 = generation.genomes[1]

    inno_num = 2 # This is the highest inno num of any gene in g1 and g2
    new_generation = Generation([])

    g3 = crossover(g1, g2, new_generation)
    #TODO: This test works! just write formal assert statements and relocate to different file