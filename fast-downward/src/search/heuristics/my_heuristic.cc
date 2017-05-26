#include "my_heuristic.h"
#include "../global_state.h"
#include "../option_parser.h"
#include "../plugin.h"
#include "../task_tools.h"

#include <cstddef>
#include <limits>
#include <utility>
#include <fstream>

/////////////////////////////////////////
#define DBFILE "../scripts/db.ssv"
////////////////////////////////////////
using namespace std;




// my_heuristic



namespace my_heuristic {

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

MyHeuristic::MyHeuristic(const Options &opts)
        :Heuristic(opts), statedb( DBFILE ){
    cout << "Initializing my heuristic..." << endl;
    pair_tz(opts.get<int>("tz_first"), opts.get<int>("tz_second"));

}

MyHeuristic::~MyHeuristic() {
}


/**********************************/

int MyHeuristic::compute_heuristic(const GlobalState &global_state) {
    State state = convert_global_state(global_state);
    if( statedb.is_state_on_path( global_state ) )
        return statedb.get_h_value( global_state );
    return std::numeric_limits<int>::max();
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
