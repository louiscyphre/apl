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

StateDB::StateDB( const std::string &dbfile ){
    std::fstream dbf;
    std::string key,value;
    dbf.open(dbfile,ios::in);
    while( dbf >> key >> value ){
        long lkey = stoul(key);
        int ival = stoi(value);
        if( !database.count( lkey ) || database[lkey] > ival )
            database[ stoul(key) ] = stoi(value);

    }
    std::cout<< "StateDB initialized!" << std::endl;
}

int StateDB::get_h( const GlobalState &state ){
    long statehash=0;
    int h=0;
    if( database.count( statehash = state.get_hash() ) ){
        h = database[statehash];
        if( h < 0 )
            return 1000;
        return h;
    }
    else
        return 10000;
}


MyHeuristic::MyHeuristic(const Options &opts)
        :Heuristic(opts),db( DBFILE ) {
    cout << "Initializing my heuristic..." << endl;
    pair_tz(opts.get<int>("tz_first"), opts.get<int>("tz_second"));

}

MyHeuristic::~MyHeuristic() {
}


/**********************************/

int MyHeuristic::compute_heuristic(const GlobalState &global_state) {
    State state = convert_global_state(global_state);
    
    if( int h = db.get_h( global_state ) ){
        std::cout<< "found known state. h = " << to_string(h) << std::endl;
        return h;
    }

    if (is_goal_state(task_proxy, state))
        return 0;
    return 1;
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
