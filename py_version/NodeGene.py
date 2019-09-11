from enum import Enum

#TODO: inherit three different types from nodegene? Would remove type variable and enum class
class NodeGene:
	def __init__(self, id_t, type_t):
		self.id = id_t
		self.type = type_t
		self.value = None
		if self.type == NodeGeneTypesEnum.BIAS.value:
			self.value = 1 #This will not change


	def __hash__(self):
		return hash(self.id)

	def __eq__(self, other):
		return self.id == other.id

	def __str__(self):
		return "ID: {:d}, TYPE: {:d}".format(self.id, self.type)



class NodeGeneTypesEnum(Enum):
	INPUT = 1
	BIAS = 2
	HIDDEN = 3
	OUTPUT = 4




