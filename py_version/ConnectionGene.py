from NodeGene import NodeGene, NodeGeneTypesEnum


# Class representing a directed connection between two NodeGenes
class ConnectionGene:

	def __init__(self, in_node_t, out_node_t, weight_t, enabled_t, inno_num_t):
		self.in_node = in_node_t  # This and out_node are references
		self.out_node= out_node_t
		self.weight = weight_t
		self.enabled = enabled_t
		self.inno_num = inno_num_t









