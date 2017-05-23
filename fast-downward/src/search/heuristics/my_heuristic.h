#ifndef HEURISTICS_MY_HEURISTIC_H
#define HEURISTICS_MY_HEURISTIC_H

#include "../heuristic.h"
#include "../global_state.h"




namespace my_heuristic {

class MyHeuristic : public Heuristic {
   
    int goal_count_square( const GlobalState &global_state );

protected:
    virtual int compute_heuristic(const GlobalState &global_state);
public:
    MyHeuristic(const options::Options &options);
    ~MyHeuristic();
};
}

#endif
