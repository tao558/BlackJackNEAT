class NodeGene:
	def __init__(self, id_t):
		self.id = id_t


	def __hash__(self):
		return hash(self.id)

	def __eq__(self, other):
		return self.id == other.id

	def __str__(self):
		return "ID: {:d}, TYPE: {}".format(self.id, type(self))


class InputNode(NodeGene):
	def __init__(self, id_t):
		NodeGene.__init__(self, id_t)
		self.value = None  #We dont have a value yet!
		self.order = 1


class BiasNode(InputNode):
	def __init__(self, id_t):
		InputNode.__init__(self, id_t)
		self.value = 1  #Update this from the InputNode. This will NEVER change


class HiddenNode(NodeGene):
	def __init__(self, id_t):
		NodeGene.__init__(self, id_t)
		self.value = None  
		self.order = 2


class OutputNode(NodeGene):
	def __init__(self, id_t):
		NodeGene.__init__(self, id_t)
		self.value = None 
		self.order = 3










class NodeGeneTypesEnum(Enum):
	INPUT = 1
	BIAS = 2
	HIDDEN = 3
	OUTPUT = 4




