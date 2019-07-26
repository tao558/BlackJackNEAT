
class NodeGene {



private:
	int id;
	TYPE type;




public:

	NodeGene(int id_temp, TYPE type_t){
		id = id_temp;
		type = type_t;
	}


	const int get_id() const {
		return id;
	}


	const TYPE get_type() const {
		return type;
	}


	friend class Genome;

	

};


	