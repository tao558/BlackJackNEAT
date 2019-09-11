from NodeGene import *


# Class representing a directed connection between two NodeGenes
class ConnectionGene:

	def __init__(self, in_node_t, out_node_t, weight_t, enabled_t, inno_num_t):
		self.in_node = in_node_t  # This and out_node are references
		self.out_node = out_node_t
		self.weight = weight_t
		self.enabled = enabled_t
		self.inno_num = inno_num_t


	def __hash__(self):
		return hash((self.in_node, self.out_node))

	def __eq__(self, other):
		return (self.in_node, self.out_node) == (other.in_node, other.out_node)

	def __str__(self):
		in_id = self.in_node.id
		out_id = self.out_node.id
		w = self.weight
		enabled = self.enabled
		inno_num = self.inno_num
		
		return ('IN: {:d}, OUT: {:d}, WEIGHT: {:f}, ENABLED: {} '
		'INNO_NUM: {:d}').format(in_id, out_id, w, enabled, inno_num)










