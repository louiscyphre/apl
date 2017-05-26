#ifndef HEURISTICS_LM_CUT_HEURISTIC_H
#define HEURISTICS_LM_CUT_HEURISTIC_H

#include "../heuristic.h"

#include <memory>

class GlobalState;

namespace options {
class Options;
}

namespace lm_cut_heuristic {

/////////////////////////////////////////////////    
class StateDB{
    std::unordered_map<long,int> database;
    public:
        StateDB( const std::string &file_name );
        bool is_state_on_path( const GlobalState &state );
        int get_h_value( const GlobalState &state );
};    
////////////////////////////////////////////////
    
class LandmarkCutLandmarks;

class LandmarkCutHeuristic : public Heuristic {
    std::unique_ptr<LandmarkCutLandmarks> landmark_generator;
    
    //////////////////
    StateDB statedb;
    /////////////////
    
    virtual int compute_heuristic_(const GlobalState &global_state) override;
    int compute_heuristic_(const State &state);
public:
    explicit LandmarkCutHeuristic(const options::Options &opts);
    virtual ~LandmarkCutHeuristic() override;
};
}

#endif
