#include "heuristic.h"

#include "evaluation_context.h"
#include "evaluation_result.h"
#include "global_operator.h"
#include "globals.h"
#include "option_parser.h"
#include "plugin.h"

#include "tasks/cost_adapted_task.h"

#include <cassert>
#include <cstdlib>
#include <limits>


Heuristic::Heuristic(const Options &opts)
    : description(opts.get_unparsed_config()),
      heuristic_cache(HEntry(NO_VALUE, true)), //TODO: is true really a good idea here?
      cache_h_values(opts.get<bool>("cache_estimates")),
      reuse_h_cache(opts.get<bool>("reuse_cache")),
      init_h_db_called(false),
      task(opts.get<shared_ptr<AbstractTask>>("transform")),
      task_proxy(*task) {
}

Heuristic::~Heuristic() {
}

HeuristicsDB::HeuristicsDB(const options::Options &options)
    :  cache_db_file_path(opts.get<bool>("cache_db_file_path")) {
}

void HeuristicsDB::init() throw DBException {
    std::fstream database_file;
    std::string key, value;
    database_file.open(cache_db_file_path, std::ios::in);
    
    if (!database_file.is_open()) {
        throw DBException();
    }
    while( database_file >> key >> value ) {
        long state_h = std::stoul(key);
        int heu_value = std::stoi(value);
        if ( !counter.count( state_h ) ){
            counter[ state_h ] = 1;
            database[ state_h ] = heu_value;
        } else {
            counter[ state_h ] += 1;
            database[ state_h ] += heu_value;
        }
    }
    for( auto it : database ){
        database[ it.first ] = database[ it.first ] / counter[ it.first ];
    }
    std::cout<< "HeuristicsDB initialized!" << std::endl;
}


void Heuristic::init_h_db()  {
    try {
        HeuristicsDB::init();
    } catch (DBException &e) {
         std::err << "Critical error: HeuristicsDB exception caught! Database file not found."
                      << std::endl;
         reuse_h_cache = false;        
    } 
    init_h_db_called = true;
}


void Heuristic::set_preferred(const GlobalOperator *op) {
    preferred_operators.insert(op);
}

void Heuristic::set_preferred(const OperatorProxy &op) {
    set_preferred(op.get_global_operator());
}

bool Heuristic::notify_state_transition(
    const GlobalState & /*parent_state*/,
    const GlobalOperator & /*op*/,
    const GlobalState & /*state*/) {
    return false;
}

State Heuristic::convert_global_state(const GlobalState &global_state) const {
    State state(*g_root_task(), global_state.get_values());
    return task_proxy.convert_ancestor_state(state);
}

void Heuristic::add_options_to_parser(OptionParser &parser) {
    parser.add_option<shared_ptr<AbstractTask>>(
        "transform",
        "Optional task transformation for the heuristic."
        " Currently, adapt_costs() and no_transform() are available.",
        "no_transform()");
    parser.add_option<bool>("cache_estimates", "cache heuristic estimates", "true");
    parser.add_option<bool>("reuse_cache", "reuse heuristic cache. This only relevant"
                                                    " for rerunning planner on the same problem more than"
                                                    " once in a row.", "true");
    parser.add_option<const std::string>("cache_db_file_path", "path to file with cache"
                                                                         "estimates per  state", 
                                                                         HeuristicDB::default_db_file);
}

// This solution to get default values seems nonoptimal.
// This is currently only used by the LAMA/FF synergy.
Options Heuristic::default_options() {
    Options opts = Options();
    opts.set<shared_ptr<AbstractTask>>("transform", g_root_task());
    opts.set<bool>("cache_estimates", false);
    opts.set<bool>("reuse_cache", false);
    opts.set<const std::string>("cache_db_file_path", HeuristicDB::default_db_file);
    return opts;
}

EvaluationResult Heuristic::compute_result(EvaluationContext &eval_context) {
    EvaluationResult result;

    assert(preferred_operators.empty());

    const GlobalState &state = eval_context.get_state();
    bool calculate_preferred = eval_context.get_calculate_preferred();

    int heuristic = NO_VALUE;

    if (!calculate_preferred && cache_h_values &&
        heuristic_cache[state].h != NO_VALUE && !heuristic_cache[state].dirty) {
        heuristic = heuristic_cache[state].h;
        result.set_count_evaluation(false);
    } else {
        heuristic = compute_heuristic(state);
        if (cache_h_values) {
            heuristic_cache[state] = HEntry(heuristic, false);
        }
        result.set_count_evaluation(true);
    }
    //TODO the code with heuristics db will be probably here, or might be added in
    //              previous if
    
//////
    //cout<< to_string( state.get_hash() ) + " " + to_string( heuristic ) <<endl;
/////
    assert(heuristic == DEAD_END || heuristic >= 0);

    if (heuristic == DEAD_END) {
        /*
          It is permissible to mark preferred operators for dead-end
          states (thus allowing a heuristic to mark them on-the-fly
          before knowing the final result), but if it turns out we
          have a dead end, we don't want to actually report any
          preferred operators.
        */
        preferred_operators.clear();
        heuristic = EvaluationResult::INFTY;
    }

#ifndef NDEBUG
    if (heuristic != EvaluationResult::INFTY) {
        for (const GlobalOperator *op : preferred_operators)
            assert(op->is_applicable(state));
    }
#endif

    result.set_h_value(heuristic);
    result.set_preferred_operators(preferred_operators.pop_as_vector());
    assert(preferred_operators.empty());

    return result;
}

string Heuristic::get_description() const {
    return description;
}


static PluginTypePlugin<Heuristic> _type_plugin(
    "Heuristic",
    "A heuristic specification is either a newly created heuristic "
    "instance or a heuristic that has been defined previously. "
    "This page describes how one can specify a new heuristic instance. "
    "For re-using heuristics, see OptionSyntax#Heuristic_Predefinitions.\n\n"
    "Definitions of //properties// in the descriptions below:\n\n"
    " * **admissible:** h(s) <= h*(s) for all states s\n"
    " * **consistent:** h(s) <= c(s, s') + h(s') for all states s "
    "connected to states s' by an action with cost c(s, s')\n"
    " * **safe:** h(s) = infinity is only true for states "
    "with h*(s) = infinity\n"
    " * **preferred operators:** this heuristic identifies "
    "preferred operators ");
