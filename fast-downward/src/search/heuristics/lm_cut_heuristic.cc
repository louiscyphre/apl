#include "lm_cut_heuristic.h"

#include "lm_cut_landmarks.h"

#include "../option_parser.h"
#include "../plugin.h"
#include "../task_proxy.h"
#include "../task_tools.h"

#include "../utils/memory.h"

#include <iostream>
#include <fstream>
/////////////////////////////////////////
#define DBFILE "../scripts/db.ssv"
////////////////////////////////////////

using namespace std;

namespace lm_cut_heuristic {

//////////////////////////////////////////////////////

StateDB::StateDB( const std::string &file_name ){
    std::fstream dbfile;
    std::string key,value;
    dbfile.open(file_name,ios::in);
    while( dbfile >> key >> value ){
        long lkey = stoul(key);
        int ival = stoi(value);
        if( !database.count( lkey ) || database[lkey] > ival )
            database[ stoul(key) ] = stoi(value);
    }
    std::cout<< "StateDB initialized!" << std::endl;
}

//////////////////////////////////////////////////////

bool StateDB::is_state_on_path( const GlobalState &state ){
    if( database.count( state.get_hash() ) )
        return true;
    return false;
}   
    
//////////////////////////////////////////////////////
    
int StateDB::get_h_value( const GlobalState &state ){
    int h = database[ state.get_hash()];
    return h;
}

///////////////////////////////////////////////////////

LandmarkCutHeuristic::LandmarkCutHeuristic(const Options &opts)
    : Heuristic(opts),
      landmark_generator(utils::make_unique_ptr<LandmarkCutLandmarks>(task_proxy)), statedb( DBFILE ){
    cout << "Initializing landmark cut heuristic..." << endl;
}

LandmarkCutHeuristic::~LandmarkCutHeuristic() {
}

int LandmarkCutHeuristic::compute_heuristic(const GlobalState &global_state) {
    State state = convert_global_state(global_state);
/////////////////////////////////////////////////////
    int h=0;
    if( statedb.is_state_on_path( global_state ) ){
        if( (h = statedb.get_h_value( global_state )) > 500 ){
            return h;
        }
        return 30000;
    }
/////////////////////////////////////////////////////
    return compute_heuristic(state);
}

int LandmarkCutHeuristic::compute_heuristic(const State &state) {
    int total_cost = 0;
    bool dead_end = landmark_generator->compute_landmarks(
        state,
        [&total_cost](int cut_cost) {total_cost += cut_cost; },
        nullptr);

    if (dead_end)
        return DEAD_END;
    return total_cost;
}

static Heuristic *_parse(OptionParser &parser) {
    parser.document_synopsis("Landmark-cut heuristic", "");
    parser.document_language_support("action costs", "supported");
    parser.document_language_support("conditional effects", "not supported");
    parser.document_language_support("axioms", "not supported");
    parser.document_property("admissible", "yes");
    parser.document_property("consistent", "no");
    parser.document_property("safe", "yes");
    parser.document_property("preferred operators", "no");

    Heuristic::add_options_to_parser(parser);
    Options opts = parser.parse();
    if (parser.dry_run())
        return nullptr;
    else
        return new LandmarkCutHeuristic(opts);
}

static Plugin<Heuristic> _plugin("lmcut", _parse);
}
