from enum import Enum

#TODO: make these getters and setters more encapsulated?
#TODO: inherit three different types from nodegene?
class NodeGene:
	def __init__(self, id_t, type_t, enabled_t):
		self.id = id_t
		self.type = type_t
		self.enabled = enabled_t


	def get_id(self):
		return self.id


	def get_type(self):
		return self.type



















# class NodeGene {



# private:
# 	int id;
# 	TYPE type;




# public:

# 	NodeGene(int id_temp, TYPE type_t){
# 		id = id_temp;
# 		type = type_t;
# 	}


# 	const int get_id() const {
# 		return id;
# 	}


# 	const TYPE get_type() const {
# 		return type;
# 	}


# 	friend class Genome;

	

# };


	