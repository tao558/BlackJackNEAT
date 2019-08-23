from NodeGene import NodeGene, NodeGeneTypesEnum
import numpy as np
from ConnectionGene import ConnectionGene


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
			if (node.type == NodeGeneTypesEnum.INPUT.value):
				n_input_nodes += 1
			elif (node.type == NodeGeneTypesEnum.HIDDEN.value):
				n_hidden_nodes += 1
			else:
				n_output_nodes += 1

		self.n_input_nodes = n_input_nodes
		self.n_hidden_nodes = n_hidden_nodes
		self.n_output_nodes = n_output_nodes

		


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



	# Adds a connection to the genome. If already fully connected, does nothing
	def mutate_add_connection(self, inno_num):
		# First check if we can even add a connection
		if (self.is_fully_connected()):
			print("THIS RAN")
			return inno_num


		OUTPUT = NodeGeneTypesEnum.OUTPUT.value
		INPUT = NodeGeneTypesEnum.INPUT.value

		while (True):

			node1 = self.nodes[np.random.randint(len(self.nodes))]
			node2 = self.nodes[np.random.randint(len(self.nodes))]
			(con_exists, is_active) = self.con_exists(node1, node2)
			
			# TODO: Check this/abbreviate it.
			# Keep it if its either a new connection or an old, disabled connection
			# it must also be a valid connection (inputs cant connect to inputs, etc)
			if ( (not con_exists or not is_active) and node1.type <= node2.type and node1.type != OUTPUT and node2.type != INPUT):
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
		
		new_node = NodeGene(self.next_node_id, NodeGeneTypesEnum.HIDDEN.value)
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


