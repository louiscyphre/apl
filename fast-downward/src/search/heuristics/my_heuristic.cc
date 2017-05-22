#include "my_heuristic.h"
#include "../global_state.h"
#include "../option_parser.h"
#include "../plugin.h"
#include "../task_tools.h"

#include <cstddef>
#include <limits>
#include <utility>
#include <fstream>
using namespace std;




// my_heuristic

#define DBFILE "../scripts/db.ssv"


namespace my_heuristic {

HeuristicsDB::HeuristicsDB( const std::string &dbfile ){
    std::fstream dbf;
    std::string key,value;
    dbf.open(dbfile,ios::in);
    while( dbf >> key >> value ){
        long state_h = stoul(key);
        int heu_value = stoi(value);
        if( !counter.count( state_h ) ){
            counter[ state_h ] = 1;
            database[ state_h ] = heu_value;
        }
        else{
            counter[ state_h ] += 1;
            database[ state_h ] += heu_value;
        }
    }
    for( auto it : database ){
        database[ it.first ] = database[ it.first ] / counter[ it.first ];
    }
    std::cout<< "HeuristicsDB initialized!" << std::endl;
}

int HeuristicsDB::get_h_from_db( const GlobalState &state ){
    long state_h=0;
    int h=0;
    if( database.count( state_h = state.get_hash() ) ){
        h = database[state_h];
        return h;
    }
    else
        return 0; 
            //std::numeric_limits<int>::max(); 
}


MyHeuristic::MyHeuristic(const Options &opts)
        :Heuristic(opts),db( DBFILE ) {
    cout << "Initializing my heuristic..." << endl;
    pair_tz(opts.get<int>("tz_first"), opts.get<int>("tz_second"));

}

MyHeuristic::~MyHeuristic() {
}


/**********************************/

int MyHeuristic::gcsquare( const GlobalState &global_state ){
    const State state = convert_global_state(global_state);
    int unsatisfied_goal_count = 0;

    for (FactProxy goal : task_proxy.get_goals()) {
        const VariableProxy var = goal.get_variable();
        if (state[var] != goal) {
            ++unsatisfied_goal_count;
        }
    }
    return unsatisfied_goal_count*unsatisfied_goal_count;
}




int MyHeuristic::compute_heuristic(const GlobalState &global_state) {
    State state = convert_global_state(global_state);
    int h = db.get_h_from_db( global_state );
    if( !h )
        return gcsquare( global_state );
    return h;
}

/************************************/


static Heuristic *_parse(OptionParser &parser) {
    Heuristic::add_options_to_parser(parser);
    parser.add_option<int>("tz_first", "first tz", "123456789");
    parser.add_option<int>("tz_second", "second tz", "123456789");
    Options opts = parser.parse();
    if (parser.dry_run())
        return 0;
    else
        return new MyHeuristic(opts);
}

static Plugin<Heuristic> _plugin("my_heuristic", _parse);
}
