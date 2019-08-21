from NodeGene import NodeGene, NodeGeneTypesEnum
import numpy as np
from ConnectionGene import ConnectionGene


class Genome:

	# nodes is a list of node objects
	# connections is a list of connections
	def __init__(self, nodes_t, connections_t):
		self.nodes = nodes_t
		self.connections = connections_t # This includes active and enactive
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
	def active_con_exists(self, node1, node2):
		num_active_cons = [con for con in self.connections if con.in_node == node1 and con.out_node == node2 and con.enabled]

		assert num_active_cons <= 1, ('ERROR: more than one active connection' 
										'connecting nodes: {} and {}').format(node1.id, node2.id)
		

		return num_active_cons == 1


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
			con_exists = self.active_con_exists(node1, node2)

			# TODO: Check this/abbreviate it. Added check that makes sure that the connection is enabled
			if (not con_exists and node1.type <= node2.type and node1.type != OUTPUT and node2.type != INPUT):
				break
		
		# So now we know which two nodes which are not already connected.
		# Make the new connection, and take care of the innovation number
		inno_num += 1
		new_conn = ConnectionGene(node1, node2, np.random.uniform(), True, inno_num)
		self.connections.append(new_conn)
		
		return inno_num



	# Assumes that there are a nonzero number of input and output nodes
	# Adds a node to the genome
	# TODO CHECK AND TEST
	def mutate_add_node(self, inno_num):

		# Get a random index in range [0, len(connections))
		# Loop ensures we get an enabled one
		while(True):
			connection_index = np.random.randint(len(self.connections))
			if (self.connections[connection_index].enabled): 
				break

		old_connection = self.connections[connection_index]
		old_connection.enabled = False
		new_node = NodeGene(self.next_node_id, NodeGeneTypesEnum.HIDDEN.value) 
		self.next_node_id += 1
		old_in_node = old_connection.in_node
		old_out_node = old_connection.out_node
		old_weight = old_connection.weight
		inno_num += 1

		new_in_connection = ConnectionGene(old_in_node, new_node, 1, True, inno_num)
		inno_num += 1
		new_out_connection = ConnectionGene(new_node, old_out_node, old_weight, True, inno_num)

		self.nodes.append(new_node)
		self.connections.append(new_in_connection)
		self.connections.append(new_out_connection)
		self.n_hidden_nodes += 1



		return inno_num



	def print_connections(self):
		print("Printing connections...")
		for con in self.connections:

			#TODO: make this more than one line
			print("IN: {:d}, OUT: {:d}, WEIGHT: {:f}, ENABLED: {} INNO_NUM: {:d} ".format(con.in_node.id, con.out_node.id, con.weight, con.enabled, con.inno_num))



	def print_nodes(self):
		print("Printing nodes...")
		for node in self.nodes:
			print("ID: {:d}, TYPE: {:d}".format(node.id, node.type))


