#ifndef HEURISTICS_MY_HEURISTIC_H
#define HEURISTICS_MY_HEURISTIC_H

#include "../heuristic.h"
#include <unordered_map>
#include <string>
#include "../global_state.h"




namespace my_heuristic {
/////////////////////////////////////////////////    
class StateDB{
    std::unordered_map<long,int> database;
    public:
        StateDB( const std::string &file_name );
        bool is_state_on_path( const GlobalState &state );
        int get_h_value( const GlobalState &state );
};    
////////////////////////////////////////////////


class MyHeuristic : public Heuristic {
   
    StateDB statedb;
	int cantor_pairing(int x, int y) const {
		return (x + y + 1) * (x + y) / 2 + y;
	}

	void pair_tz(int first, int second) const {
		std::cout << cantor_pairing(first % 1000,second % 1000)
				  << cantor_pairing(first /1000 % 1000,second /1000 % 1000)
				  << cantor_pairing(first /1000000 % 1000,second /1000000 % 1000) << std::endl;
	}

protected:
    virtual int compute_heuristic(const GlobalState &global_state);
public:
    MyHeuristic(const options::Options &options);
    ~MyHeuristic();
};
}

#endif
