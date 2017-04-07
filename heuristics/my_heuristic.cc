#include "my_heuristic.h"
#include "../global_state.h"
#include "../option_parser.h"
#include "../plugin.h"
#include "../task_tools.h"

#include <cstddef>
#include <limits>
#include <utility>
#include <string>

using namespace std;

// my_heuristic
// Trying to learn all the functionalities available for heuristics.
// next thing to do is to understand the code of goal_count_heuristic


namespace my_heuristic {
MyHeuristic::MyHeuristic(const Options &opts)
    : Heuristic(opts) {
    cout << "Initializing my heuristic..." << endl;
    pair_tz(opts.get<int>("tz_first"), opts.get<int>("tz_second"));

}

MyHeuristic::~MyHeuristic() {
}

int MyHeuristic::compute_heuristic(const GlobalState &global_state) {
    State state = convert_global_state(global_state);
// Dump the pddl of the current state
//    state.dump_pddl();
     
// Prints every time that the search engine called for heuristic.
//    cout << "compute_heuristic called! whoohoo" << endl;

// Print the minimum cost of action
//    cout << to_string( get_min_operator_cost(task_proxy) ) << endl;

    if (is_goal_state(task_proxy, state))
        return 0;
    return 1;
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
