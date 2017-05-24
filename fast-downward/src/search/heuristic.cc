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
#include <fstream>

Heuristic::Heuristic(const Options &opts)
    : db(opts),
      description(opts.get_unparsed_config()),
      heuristic_cache(HEntry(NO_VALUE, true)), //TODO: is true really a good idea here?
      cache_h_values(opts.get<bool>("cache_estimates")),
      use_hdb(opts.get<bool>("use_hdb")),
      init_hdb_called(false),
      task(opts.get<std::shared_ptr<AbstractTask>>("transform")),
      task_proxy(*task) {
}

Heuristic::~Heuristic() {
}

Heuristic::HeuristicsDB::HeuristicsDB(const options::Options &opts)
    : hdb_file_path(opts.get<const std::string>("hdb_file_path")) {
}

void Heuristic::HeuristicsDB::init() throw (DBException) {
    std::fstream database_file;
    std::string key, value;
    database_file.open(hdb_file_path, std::ios::in);
    
    if (!database_file.is_open()) {
        throw DBException();
    }
    while( database_file >> key >> value ) {
        long state_hash = std::stoul(key);
        int heuristic = std::stoi(value);
        if ( !counter.count( state_hash ) ){
            counter[ state_hash ] = 1;
            database[ state_hash ] = heuristic;
        } else {
            counter[ state_hash ] += 1;
            database[ state_hash ] += heuristic;
        }
    }
    for( auto it : database ){
        database[ it.first ] = database[ it.first ] / counter[ it.first ];
    }
    std::cout<< "HeuristicsDB initialized!" << std::endl;
}


int Heuristic::HeuristicsDB::get_heuristic(const GlobalState &global_state) {
    const State state = convert_global_state(global_state);                         
    long hash = state.get_hash();

    if (database.find(hash) == database.end()) {
        return 0;
    }
    return database[hash];
}


void Heuristic::HeuristicsDB::add_heuristic(const GlobalState &global_state,
                                const int heuristic) {
    const State state = convert_global_state(global_state);                             
    long hash = state.get_hash();
    database[hash] = heuristic;
}

void Heuristic::init_hdb()  {
    try {
        HeuristicsDB::init();
    } catch (DBException &e) {
         std::err << "Critical error: HeuristicsDB exception caught!"
         std::err << "Database file not found."
                  << std::endl;
         use_hdb  = false;        
    } 
    init_hdb_called = true;
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
    parser.add_option<std::shared_ptr<AbstractTask>>(
        "transform",
        "Optional task transformation for the heuristic."
        " Currently, adapt_costs() and no_transform() are available.",
        "no_transform()");
    parser.add_option<bool>("cache_estimates",
                            "cache heuristic estimates", "true");
    parser.add_option<bool>("use_hdb", "use heuristic database."
                            " This only relevant for rerunning planner on the"
                            " same problem more than once in a row.", "true");
    parser.add_option<const std::string>("hdb_file_path", 
                                         "path to file with cache"
                                         " estimates per state", 
                                         HeuristicDB::default_db_file);
}

// This solution to get default values seems nonoptimal.
// This is currently only used by the LAMA/FF synergy.
Options Heuristic::default_options() {
    Options opts = Options();
    opts.set<std::shared_ptr<AbstractTask>>("transform", g_root_task());
    opts.set<bool>("cache_estimates", false);
    opts.set<bool>("use_hdb", false);
    opts.set<const std::string>("hdb_file_path", HeuristicDB::default_db_file);
    return opts;
}

EvaluationResult Heuristic::compute_result(EvaluationContext &eval_context) {
    EvaluationResult result;

    assert(preferred_operators.empty());

    const GlobalState &state = eval_context.get_state();
    bool calculate_preferred = eval_context.get_calculate_preferred();

    int heuristic = NO_VALUE;

    if (use_hdb && !init_hdb_called) {
        this.init_hdb();
    }
    if (!calculate_preferred && cache_h_values &&
        heuristic_cache[state].h != NO_VALUE && !heuristic_cache[state].dirty) {
        heuristic = heuristic_cache[state].h;
        result.set_count_evaluation(false);
    } else {
        if (use_hdb) {
            heuristic = db.get_heuristic(state);
            if (!heuristic) {
                heuristic = compute_heuristic(state);
                db.add_heuristic(state, heuristic);
            }
        } else {
            heuristic = compute_heuristic(state);
        }
        if (cache_h_values) {
            heuristic_cache[state] = HEntry(heuristic, false);
        }
        result.set_count_evaluation(true);
    }
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

std::string Heuristic::get_description() const {
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
