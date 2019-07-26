#include <vector>
#include "ConnectionGene.h"  //This has NodeGene as a dependency.
#include <cstdlib>
#include <map>






class Genome {


private:
	std::vector<NodeGene> nodes;
	std::vector<ConnectionGene> connections;
	unsigned int* innovation_count_ptr;
	std::map<TYPE, int> type_counts;


	

	

	/* Takes in two NodeGenes and returns whether a connection exists between them already.
	Might want to rewrite this with an == operator for ConnectionGenes
	*/
	const bool connection_exists(NodeGene first, NodeGene second) const {
		for (unsigned int i=0; i<connections.size(); i++) {
			ConnectionGene c = connections[i];
			if (c.in.id == first.id && c.out.id == second.id)
				return true;
		}
		return false;

	}

	const bool fully_connected() const{ 
		int n_i = type_counts[INPUT];
		int n_h = type_counts[HIDDEN];
		int n_o = type_counts[OUTPUT];

		int max_num_connections = n_i * (n_h + n_o) + n_h * (n_h + n_o);
		return (connections.size() == max_num_connections);
	}




	void add_connection() {
		if (this -> fully_connected()) {
			return;
		}		

		/* Get two random nodes. I think the default assignment operator should work fine here. 
		I dont want to create a new object. Keep getting two random nodes until one has a higher type
		than the other */

		//TODO: WRITE COPY CONSTRUCTOR AND ASSIGNMENT OPERATOR.
		NodeGene first = nodes[rand() % nodes.size()];
		NodeGene second = nodes[rand() % nodes.size()];

		bool found_pair = false;
		while (!found_pair) {
			if (first.get_type() == second.get_type() && first.get_type() != HIDDEN) {
				first = nodes[rand() % nodes.size()];
				second = nodes[rand() % nodes.size()];
				continue;

			} 


			//Now lets check if they need to be switched so that first is "in" and second is "out"
			if (first.get_type() > second.get_type()) {
				NodeGene tmp = first;
				first = second;
				second = tmp;

			}

			/*	At this point, we have two nodes that are correctly spaced 
			(the first and second are either different, or the same but in the hidden layer)
			and first is the "in" node, and the second is the "out" node. Now lets check if such a connection already exists.
			*/

			if (connection_exists(first, second)) {
				first = nodes[rand() % nodes.size()];
				second = nodes[rand() % nodes.size()];
				continue;
			}

			found_pair = true;

		}

		//If the above passes, lets add the new connection!
		(*innovation_count_ptr)++;
		ConnectionGene new_connection(first, second, ((float) rand() / (float) RAND_MAX), true, *innovation_count_ptr);
		connections.push_back(new_connection);


	}


	//Will the genome be initialized with connections or will connections.size() == 0? 
	//Will have to handle that edge case then.
	void add_node() {
		int rand_index;

		bool found_enabled_connection = false;
		while(!found_enabled_connection) {
			rand_index = rand() % connections.size();
			if (connections[rand_index].enabled) {
				found_enabled_connection = true;
			}
		}


		connections[rand_index].enabled = false;

		NodeGene old_in = connections[rand_index].in;
		NodeGene old_out = connections[rand_index].out;
		float old_weight = connections[rand_index].weight;

		NodeGene new_node(nodes.size(), HIDDEN);
		nodes.push_back(new_node);


		(*innovation_count_ptr)++;
		ConnectionGene first_half(old_in, new_node, 1, true, *innovation_count_ptr);
		(*innovation_count_ptr)++;
		ConnectionGene second_half(new_node, old_out, old_weight, true, *innovation_count_ptr);


		connections.push_back(first_half);
		connections.push_back(second_half);

	}


public:


	//BE SURE TO CHANGE THIS LATER ONCE YOU FIGURE OUT HOW MANY INPUTS AND OUTPUTS ARE NECESSARY
	Genome() {
		type_counts[INPUT] = 0;
		type_counts[HIDDEN] = 0;
		type_counts[OUTPUT] = 0;

	}




	void print_connections(){
		for (int i=0; i<connections.size(); i++) {
    		std::cout << "in: " << connections[i].in.id << " out: " << connections[i].out.id << " "  <<  connections[i].innovation_num << std::endl;
    
    	}
	}


	void print_nodes(){
		for (int i=0; i<nodes.size(); i++) {
    		std::cout << "id: " << nodes[i].id << std::endl;
    
    	}
	}


	

};