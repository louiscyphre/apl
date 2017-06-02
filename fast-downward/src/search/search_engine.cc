#include "search_engine.h"

#include "evaluation_context.h"
#include "globals.h"
#include "option_parser.h"
#include "plugin.h"

#include "algorithms/ordered_set.h"

#include "utils/countdown_timer.h"
#include "utils/system.h"
#include "utils/timer.h"

#include <cassert>
#include <iostream>
#include <limits>
#include <algorithm>

using namespace std;
using utils::ExitCode;


SearchEngine::SearchEngine(const Options &opts)
    : status(IN_PROGRESS),
      solution_found(false),
      state_registry(
          *g_root_task(), *g_state_packer, *g_axiom_evaluator, g_initial_state_data),
      search_space(state_registry,
                   static_cast<OperatorCost>(opts.get_enum("cost_type"))),
      cost_type(static_cast<OperatorCost>(opts.get_enum("cost_type"))),
      max_time(opts.get<double>("max_time")) {
    if (opts.get<int>("bound") < 0) {
        cerr << "error: negative cost bound " << opts.get<int>("bound") << endl;
        utils::exit_with(ExitCode::INPUT_ERROR);
    }
    bound = opts.get<int>("bound");
    
    // #apl Nathan & Michael START ------>
    if (opts.get<double>("threshold") < 0.0 || 
        opts.get<double>("threshold") > 1.0) {
        cerr << "error: search threshold must be between 0.0 and 1.0" << endl;
        utils::exit_with(ExitCode::INPUT_ERROR);
    }
    threshold = opts.get<double>("threshold");

    pre_phase = false;
    // #apl Nathan & Michael END <------
}

SearchEngine::~SearchEngine() {
}

void SearchEngine::print_statistics() const {
    cout << "Bytes per state: "
         << state_registry.get_state_size_in_bytes() << endl;
}

bool SearchEngine::found_solution() const {
    return solution_found;
}

SearchStatus SearchEngine::get_status() const {
    return status;
}

const SearchEngine::Plan &SearchEngine::get_plan() const {
    assert(solution_found);
    return plan;
}

void SearchEngine::set_plan(const Plan &p) {
    solution_found = true;
    plan = p;
}

// #apl Nathan & Michael START ------>
void SearchEngine::set_for_pre_phase(const Plan &p, int cost) {
    pre_phase = true;
    // We are reversing the plan so we can easily use "pop" later.
    last_plan = p;
    current_phase_op = last_plan.begin();
    last_plan_cost = cost;
}
// #apl Nathan & Michael END <------

void SearchEngine::search() {
    initialize();
    // #apl Nathan & Michael START ------>
    cout << "Current search threshold: " << threshold << endl;
    // #apl Nathan & Michael END <------
    utils::CountdownTimer timer(max_time);
    while (status == IN_PROGRESS) {
        status = step();
        if (timer.is_expired()) {
            cout << "Time limit reached. Abort search." << endl;
            status = TIMEOUT;
            break;
        }
    }
    // TODO: Revise when and which search times are logged.
    cout << "Actual search time: " << timer
         << " [t=" << utils::g_timer << "]" << endl;
}

bool SearchEngine::check_goal_and_set_plan(const GlobalState &state) {
    if (test_goal(state)) {
        cout << "Solution found!" << endl;
        Plan plan;
        search_space.trace_path(state, plan);
        set_plan(plan);
        return true;
    }
    return false;
}

void SearchEngine::save_plan_if_necessary() const {
    if (found_solution())
        save_plan(get_plan());
}

int SearchEngine::get_adjusted_cost(const GlobalOperator &op) const {
    return get_adjusted_action_cost(op, cost_type);
}

void SearchEngine::add_options_to_parser(OptionParser &parser) {
    ::add_cost_type_option_to_parser(parser);
    parser.add_option<int>(
        "bound",
        "exclusive depth bound on g-values. Cutoffs are always performed"
        " according to the real cost, regardless of the cost_type parameter",
        "infinity");
    parser.add_option<double>(
        "max_time",
        "maximum time in seconds the search is allowed to run for. The "
        "timeout is only checked after each complete search step "
        "(usually a node expansion), so the actual runtime can be arbitrarily "
        "longer. Therefore, this parameter should not be used for time-limiting "
        "experiments. Timed-out searches are treated as failed searches, "
        "just like incomplete search algorithms that exhaust their search space.",
        "infinity");
   // #apl Nathan & Michael START ------>
    parser.add_option<double>(
        "threshold",
        "varying from 0.0 to 1.0, threshold parameter is point in the search "
        "path, from which the optimizing search will start. This option is useful when "
        "plan already found, and we want to optimize it by skipping certain "
        "part of the path up to threshold point, and start optimizing (A*) search"
        "from this point. By default, searching from initial state.",
        "0.0");
   // #apl Nathan & Michael END <------
     
}

// #apl Nathan & Michael START ------>
std::vector<const GlobalOperator *> SearchEngine::pre_phase_operator(const int &real_g){
    vector<const GlobalOperator *> vec_for_op;
    if( real_g + (*current_phase_op)->get_cost() >= threshold*last_plan_cost ){
        pre_phase = false;
        std::cout << "---------------------------------------" <<endl;
        std::cout << "Pre phase finished, starting real search." << endl;
        std::cout << "---------------------------------------" <<endl;
    }
    vec_for_op.push_back( *current_phase_op );
    ++current_phase_op;
    return vec_for_op;
}
// #apl Nathan & Michael END <------

// #apl Nathan & Michael START ------>
double SearchEngine::get_threshold() const{
    return threshold;
}
// #apl Nathan & Michael END <------

void print_initial_h_values(const EvaluationContext &eval_context) {
    eval_context.get_cache().for_each_heuristic_value(
        [] (const Heuristic *heur, const EvaluationResult &result) {
        cout << "Initial heuristic value for "
             << heur->get_description() << ": ";
        if (result.is_infinite())
            cout << "infinity";
        else
            cout << result.get_h_value();
        cout << endl;
    }
        );
}


static PluginTypePlugin<SearchEngine> _type_plugin(
    "SearchEngine",
    // TODO: Replace empty string by synopsis for the wiki page.
    "");


algorithms::OrderedSet<const GlobalOperator *> collect_preferred_operators(
    EvaluationContext &eval_context,
    const vector<Heuristic *> &preferred_operator_heuristics) {
    algorithms::OrderedSet<const GlobalOperator *> preferred_operators;
    for (Heuristic *heuristic : preferred_operator_heuristics) {
        /*
          Unreliable heuristics might consider solvable states as dead
          ends. We only want preferred operators from finite-value
          heuristics.
        */
        if (!eval_context.is_heuristic_infinite(heuristic)) {
            for (const GlobalOperator *op :
                 eval_context.get_preferred_operators(heuristic)) {
                preferred_operators.insert(op);
            }
        }
    }
    return preferred_operators;
}
