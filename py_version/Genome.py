from NodeGene import *
import numpy as np
from ConnectionGene import ConnectionGene
import copy


class Genome:

	# nodes is a list of node objects
	# connections is a list of connections
	def __init__(self, nodes_t, connections_t, generation_t):
		self.nodes = nodes_t
		self.connections = connections_t # This includes active and enactive
		self.generation = generation_t #reference to gen. this genome is in
		self.next_node_id = len(self.nodes)
		
		# Now count the number of each type of node
		n_input_nodes = n_hidden_nodes = n_output_nodes = 0
		for node in self.nodes:
			if isinstance(node, InputNode):
				n_input_nodes += 1
			elif isinstance(node, HiddenNode):
				n_hidden_nodes += 1
			else:
				n_output_nodes += 1

		self.n_input_nodes = n_input_nodes
		self.n_hidden_nodes = n_hidden_nodes
		self.n_output_nodes = n_output_nodes

		self.fitness = 0 # TODO: keep this here, or play some games first?

		


	# Returns true when a connection exists between node1 and node2
	# false otherwise. Compares ids, not actual references
	def con_exists(self, node1, node2, only_active = False):  
		num_cons = 0
		enabled = None

		for con in self.connections:
			if con.in_node == node1 and con.out_node == node2:

				if (only_active and con.enabled):
					enabled = True
					num_cons += 1

				elif (not only_active):
					enabled = con.enabled
					num_cons += 1


		# Shouldn't have more than one of the same connection
		assert num_cons <= 1, ('ERROR: more than one active connection' 
										'connecting nodes: {} and {}').format(node1.id, node2.id)

		return (num_cons == 1, enabled)
		

		


	# Returns true if a network is fully connected and false otherwise
	def is_fully_connected(self):
		n_in = self.n_input_nodes
		n_hid = self.n_hidden_nodes
		n_out = self.n_output_nodes
		#Only consider active connections!
		n_active_cons = len([con for con in self.connections if con.enabled]) 

		return (n_in * (n_hid + n_out) + n_hid * (n_hid + n_out) == n_active_cons)




	# Checks whether a connection fron n1 to n2 is valid
	# Based on types (inputs cant be connected to inputs, etc)
	def is_valid_con(self, n1, n2):
		n1_is_input = isinstance(n1, InputNode)
		n2_is_input = isinstance(n2, InputNode)
		n1_is_output = isinstance(n1, OutputNode)
		n2_is_output = isinstance(n2, OutputNode)
		
		
		return (n1.order <= n2.order and  
				not (n1_is_input and n2_is_input) and
				not (n1_is_output and n2_is_output))




	# Adds a connection to the genome. If already fully connected, does nothing
	def mutate_add_connection(self, inno_num):
		# First check if we can even add a connection
		if (self.is_fully_connected()):
			print("THIS RAN")
			return inno_num



		while (True):

			node1 = self.nodes[np.random.randint(len(self.nodes))]
			node2 = self.nodes[np.random.randint(len(self.nodes))]
			(con_exists, is_active) = self.con_exists(node1, node2)
			
			# TODO: Check this/abbreviate it.
			# Keep it if its either a new connection or an old, disabled connection
			# it must also be a valid connection (inputs cant connect to inputs, etc)
			if ( (not con_exists or not is_active) and self.is_valid_con(node1, node2) ):
				break
		

		# So now we know which two nodes we are connecting/reconnecting
		# Make the new connection and figure out if its a new innovation
		temp_con = ConnectionGene(node1, node2, None, None, None)

		# If there is a matching connection, reenable it
		if (con_exists):
			index = self.connections.index(temp_con)
			self.connections[index].enabled = True


		#Otherwise we have a brand new connection!
		else:
			inno_num += 1
			temp_con.inno_num = inno_num
			temp_con.enabled = True
			temp_con.weight = np.random.uniform()
			self.connections.append(temp_con)


		return inno_num

		


	# Assumes that there are a nonzero number
	#  of input and output nodes
	# Adds a node to the genome
	def mutate_add_node(self, inno_num):
		# Get a random index in range [0, len(connections))
		# Loop ensures we get an enabled one
		while(True):
			connection_index = np.random.randint(len(self.connections))
			if (self.connections[connection_index].enabled): 
				break

		con_to_split = self.connections[connection_index]
		con_to_split.enabled = False
		old_in_node = con_to_split.in_node
		old_out_node = con_to_split.out_node
		old_weight = con_to_split.weight
		
		new_node = HiddenNode(self.next_node_id)
		self.next_node_id += 1

		inno_num += 1
		new_in_con = ConnectionGene(old_in_node, new_node, 1, True, inno_num)
		inno_num += 1
		new_out_con = ConnectionGene(new_node, old_out_node, old_weight, True, inno_num)

		self.nodes.append(new_node)
		self.connections.append(new_in_con)
		self.connections.append(new_out_con)
		self.n_hidden_nodes += 1

		return inno_num



	def print_connections(self):
		print("Printing connections...")
		for con in self.connections:
			print(con)



	def print_nodes(self):
		print("Printing nodes...")
		for node in self.nodes:
			print(node)


# End class definition....

# This is similar to the crossover function in the origin NEAT code
# found here: https://github.com/FernandoTorres/NEAT/blob/master/src/genome.cpp
def crossover(g1, g2, new_generation):
	i1 = 0
	i2 = 0
	g1_cons = g1.connections
	g2_cons = g2.connections
	cons = list()
	nodes = set()
	g1_better = g1.fitness > g2.fitness or g1.fitness == g2.fitness and len(g1_cons) < len(g2_cons)

	while(i1 < len(g1_cons) and i2 < len(g2_cons)):
		if g1_cons[i1].inno_num == g2_cons[i2].inno_num:
			g1_chosen = np.random.uniform() < 0.5
			
			if g1_chosen:
				cons.append(copy.deepcopy(g1_cons[i1]))
				nodes.add(copy.deepcopy(g1_cons[i1].in_node))
				nodes.add(copy.deepcopy(g1_cons[i1].out_node))

			else:
				cons.append(copy.deepcopy(g2_cons[i2]))
				nodes.add(copy.deepcopy(g2_cons[i2].in_node))
				nodes.add(copy.deepcopy(g2_cons[i2].out_node))								

			i1 += 1
			i2 += 1


		elif g1_cons[i1].inno_num < g2_cons[i2].inno_num:
			if g1_better:
				cons.append(copy.deepcopy(g1_cons[i1]))
				nodes.add(copy.deepcopy(g1_cons[i1].in_node))
				nodes.add(copy.deepcopy(g1_cons[i1].out_node))
				
			i1 += 1


		else:
			if not g1_better:
				cons.append(copy.deepcopy(g2_cons[i2]))
				nodes.add(copy.deepcopy(g2_cons[i2].in_node))
				nodes.add(copy.deepcopy(g2_cons[i2].out_node))
			i2 += 1


	# Now we need to check if the more fit parent still has 
	# some genes to add
	if g1_better and i1 < len(g1_cons):
		while i1 < len(g1_cons):
			cons.append(copy.deepcopy(g1_cons[i1]))
			nodes.add(copy.deepcopy(g1_cons[i1].in_node))
			nodes.add(copy.deepcopy(g1_cons[i1].out_node))
			i1 += 1
	
	elif not g1_better and i2 < len(g2_cons): 
		while i2 < len(g2_cons):
			cons.append(copy.deepcopy(g2_cons[i2]))
			nodes.add(copy.deepcopy(g2_cons[i2].in_node))
			nodes.add(copy.deepcopy(g2_cons[i2].out_node))
			i2 += 1	

	# Now we have the cons and nodes of the new genome...
	nodes = sorted(list(nodes), key = lambda node: node.id)
	cons = sorted(cons, key = lambda con: con.inno_num)

	new_genome = Genome(nodes, cons, new_generation)
	return new_genome



# TODO: test
def compat_distance(g1, g2, c1, c2, c3):
	N = max(len(g1.connections), len(g2.connections))
	g1_inno_nums = [con.inno_num for con in g1.connections]
	g2_inno_nums = [con.inno_num for con in g2.connections]
	
	assert sorted(g1_inno_nums) == g1_inno_nums
	assert sorted(g2_inno_nums) == g2_inno_nums

	max_g1 = max(g1_inno_nums)
	max_g2 = max(g2_inno_nums)
	min_g1 = min(g1_inno_nums)
	min_g2 = min(g2_inno_nums)
	
	# count the number of disjoint and excess genes
	num_disjoint_g1 = len([n for n in g1_inno_nums if n < max_g2 and n > min_g2 and not n in g2_inno_nums])
	num_disjoint_g2 = len([n for n in g2_inno_nums if n < max_g1 and n > min_g1 and not n in g1_inno_nums])
	D = num_disjoint_g1 + num_disjoint_g2

	num_excess_g1 = len([n for n in g1_inno_nums if n > max_g2 or n < min_g2])
	num_excess_g2 = len([n for n in g2_inno_nums if n > max_g1 or n < min_g1])
	E = num_excess_g1 + num_excess_g2

	# now count the average difference in weights TODO: review probably faster way
	g1_matching_genes_weights = [con.weight for con in g1_inno_nums if con.inno_num in g2_inno_nums]
	g2_matching_genes_weights = [con.weight for con in g2_inno_nums if con.inno_num in g1_inno_nums] 
	Wbar = sum(g1_matching_genes_weights - g2_matching_genes_weights) / len(g1_matching_genes_weights)


	return c1*E/N + c2*D/N + c3*Wbar



	


