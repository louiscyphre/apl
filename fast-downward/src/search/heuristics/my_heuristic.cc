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

namespace my_heuristic {

MyHeuristic::MyHeuristic(const Options &opts)
        :Heuristic(opts)  {
    cout << "Initializing my heuristic..." << endl;
    pair_tz(opts.get<int>("tz_first"), opts.get<int>("tz_second"));
}

MyHeuristic::~MyHeuristic() {
}


int MyHeuristic::goal_count_square( const GlobalState &global_state ){
    const State state = convert_global_state(global_state);
    int unsatisfied_goal_count = 0;

    for (FactProxy goal : task_proxy.get_goals()) {
        const VariableProxy var = goal.get_variable();
        if (state[var] != goal) {
            ++unsatisfied_goal_count;
        }
    }
    return unsatisfied_goal_count * unsatisfied_goal_count;
}


int MyHeuristic::compute_heuristic(const GlobalState &global_state) {
    State state = convert_global_state(global_state);
    int h = db.get_h_from_db(global_state);
    if( !h )
        return goal_count_square(global_state);
    return h;
}

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
