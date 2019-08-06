from enum import Enum

#TODO: inherit three different types from nodegene? Would remove type variable and enum class
class NodeGene:
	def __init__(self, id_t, type_t):
		self.id = id_t
		self.type = type_t




class NodeGeneTypesEnum(Enum):
	INPUT = 1
	HIDDEN = 2
	OUTPUT = 3




