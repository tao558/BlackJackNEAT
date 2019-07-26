#include "NodeGene.h"




class ConnectionGene {

private:

	NodeGene in;
	NodeGene out;
	float weight;
	bool enabled;
	unsigned int innovation_num;





public:

	ConnectionGene(NodeGene in_t, NodeGene out_t, float weight_t, bool enabled_t, unsigned int innovation_num_t):
		in(in_t),
		out(out_t),
		weight(weight_t),
		enabled(enabled_t),
		innovation_num(innovation_num_t)

	{}


//Might not need these



	NodeGene get_in() {
		return in;
	}

	NodeGene get_out() {
		return out;
	}


	float get_weight(){
		return weight;
	}


	bool get_enabled(){
		return enabled;
	}


	int get_innovation_num(){
		return innovation_num;
	}


	friend class Genome;



};