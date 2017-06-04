def configs_optimal_core():
    return {
        # A*
        "astar_blind": [
            "--search",
            "astar(blind)"],
        "astar_h2": [
            "--search",
            "astar(hm(2))"],
        "astar_ipdb": [
            "--search",
            "astar(ipdb)"],
        "astar_lmcount_lm_merged_rhw_hm": [
            "--search",
            "astar(lmcount(lm_merged([lm_rhw(),lm_hm(m=1)]),admissible=true),mpd=true)"],
        "astar_lmcut": [
            "--search",
            "astar(lmcut)"],
        "astar_hmax": [
            "--search",
            "astar(hmax)"],
        "astar_merge_and_shrink_rl_fh": [
            "--search",
            "astar(merge_and_shrink("
            "merge_strategy=merge_strategy=merge_precomputed("
            "merge_tree=linear(variable_order=reverse_level)),"
            "shrink_strategy=shrink_fh(),"
            "label_reduction=exact(before_shrinking=false,"
            "before_merging=true),max_states=50000))"],
        "astar_merge_and_shrink_dfp_bisim": [
            "--search",
            "astar(merge_and_shrink(merge_strategy=merge_stateless("
            "merge_selector=score_based_filtering(scoring_functions=["
            "goal_relevance,dfp,total_order("
            "atomic_ts_order=reverse_level,product_ts_order=new_to_old,"
            "atomic_before_product=false)])),"
            "shrink_strategy=shrink_bisimulation(greedy=false),"
            "label_reduction=exact(before_shrinking=true,"
            "before_merging=false),max_states=50000,"
            "threshold_before_merge=1))"],
        "astar_merge_and_shrink_dfp_greedy_bisim": [
            "--search",
            "astar(merge_and_shrink(merge_strategy=merge_stateless("
            "merge_selector=score_based_filtering(scoring_functions=["
            "goal_relevance,dfp,total_order("
            "atomic_ts_order=reverse_level,product_ts_order=new_to_old,"
            "atomic_before_product=false)])),"
            "shrink_strategy=shrink_bisimulation("
            "greedy=true),"
            "label_reduction=exact(before_shrinking=true,"
            "before_merging=false),max_states=infinity,"
            "threshold_before_merge=1))"],
    }

def configs_satisficing_core():
    return {
        # A*
        "astar_goalcount": [
            "--search",
            "astar(goalcount)"],
        # eager greedy
        "eager_greedy_ff": [
            "--heuristic",
            "h=ff()",
            "--search",
            "eager_greedy([h],preferred=[h])"],
        "eager_greedy_add": [
            "--heuristic",
            "h=add()",
            "--search",
            "eager_greedy([h],preferred=[h])"],
        "eager_greedy_cg": [
            "--heuristic",
            "h=cg()",
            "--search",
            "eager_greedy([h],preferred=[h])"],
        "eager_greedy_cea": [
            "--heuristic",
            "h=cea()",
            "--search",
            "eager_greedy([h],preferred=[h])"],
        # lazy greedy
        "lazy_greedy_ff": [
            "--heuristic",
            "h=ff()",
            "--search",
            "lazy_greedy([h],preferred=[h])"],
        "lazy_greedy_add": [
            "--heuristic",
            "h=add()",
            "--search",
            "lazy_greedy([h],preferred=[h])"],
        "lazy_greedy_cg": [
            "--heuristic",
            "h=cg()",
            "--search",
            "lazy_greedy([h],preferred=[h])"],
    }


def configs_optimal_ipc():
    return {
        "seq_opt_merge_and_shrink": ["--alias", "seq-opt-merge-and-shrink"],
        "seq_opt_fdss_1": ["--alias", "seq-opt-fdss-1"],
        "seq_opt_fdss_2": ["--alias", "seq-opt-fdss-2"],
    }


def configs_satisficing_ipc():
    return {
        "seq_sat_lama_2011": ["--alias", "seq-sat-lama-2011"],
        "seq_sat_fdss_1": ["--alias", "seq-sat-fdss-1"],
        "seq_sat_fdss_2": ["--alias", "seq-sat-fdss-2"],
    }


def configs_optimal_extended():
    return {
        "astar_lmcount_lm_merged_rhw_hm_no_order": [
            "--search",
            "astar(lmcount(lm_merged([lm_rhw(),lm_hm(m=1)]),admissible=true),mpd=true)"],
        "astar_cegar": [
            "--search",
            "astar(cegar())"],
    }


def configs_satisficing_extended():
    return {
        # eager greedy
        "eager_greedy_alt_ff_cg": [
            "--heuristic",
            "hff=ff()",
            "--heuristic",
            "hcg=cg()",
            "--search",
            "eager_greedy([hff,hcg],preferred=[hff,hcg])"],
        "eager_greedy_ff_no_pref": [
            "--search",
            "eager_greedy([ff()])"],
        # lazy greedy
        "lazy_greedy_alt_cea_cg": [
            "--heuristic",
            "hcea=cea()",
            "--heuristic",
            "hcg=cg()",
            "--search",
            "lazy_greedy([hcea,hcg],preferred=[hcea,hcg])"],
        "lazy_greedy_ff_no_pref": [
            "--search",
            "lazy_greedy([ff()])"],
        "lazy_greedy_cea": [
            "--heuristic",
            "h=cea()",
            "--search",
            "lazy_greedy([h],preferred=[h])"],
        # lazy wA*
        "lazy_wa3_ff": [
            "--heuristic",
            "h=ff()",
            "--search",
            "lazy_wastar([h],w=3,preferred=[h])"],
        # eager wA*
        "eager_wa3_cg": [
            "--heuristic",
            "h=cg()",
            "--search",
            "eager(single(sum([g(),weight(h,3)])),preferred=[h])"],
        # ehc
        "ehc_ff": [
            "--search",
            "ehc(ff())"],
        # iterated
        "iterated_wa_ff": [
            "--heuristic",
            "h=ff()",
            "--search",
            "iterated([lazy_wastar([h],w=10), lazy_wastar([h],w=5), lazy_wastar([h],w=3),"
            "lazy_wastar([h],w=2), lazy_wastar([h],w=1)])"],
        # pareto open list
        "pareto_ff": [
            "--heuristic",
            "h=ff()",
            "--search",
            "eager(pareto([sum([g(), h]), h]), reopen_closed=true,"
            "f_eval=sum([g(), h]))"],
    }


def configs_satisficing_with_threshold():
    return {
        "iterated_wa_0": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,threshold=0.98,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.95,reopen_closed=false), lazy_wastar([h3,h4],w=4,threshold=0.90,reopen_closed=false), lazy_wastar([h3,h4],w=8,threshold=0.85,reopen_closed=false),lazy_wastar([h3,h4],w=16,threshold=0.80,reopen_closed=false), lazy_wastar([h3,h4],w=32,threshold=0.75,reopen_closed=false), lazy_wastar([h3,h4],w=64,threshold=0.70,reopen_closed=false),lazy_wastar([h3,h4],w=128,threshold=0.67,reopen_closed=false), lazy_wastar([h3,h4],w=256,threshold=0.65,reopen_closed=false), lazy_wastar([h3,h4],w=512,threshold=0.60,reopen_closed=false),lazy_wastar([h3,h4],w=1024,threshold=0.58,reopen_closed=false), lazy_wastar([h3,h4],w=2048,threshold=0.56,reopen_closed=false), lazy_wastar([h3,h4],w=4096,threshold=0.54,reopen_closed=false),lazy_wastar([h3,h4],w=8192,threshold=0.52,reopen_closed=false), lazy_wastar([h3,h4],w=16384,threshold=0.50,reopen_closed=false), lazy_wastar([h3,h4],w=32768,threshold=0.49,reopen_closed=false)], continue_on_fail=true)"],

        "iterated_wa_0_inverted_weights": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=32768,threshold=0.98,reopen_closed=false), lazy_wastar([h3,h4],w=16384,threshold=0.95,reopen_closed=false), lazy_wastar([h3,h4],w=8192,threshold=0.90,reopen_closed=false), lazy_wastar([h3,h4],w=4096,threshold=0.85,reopen_closed=false),lazy_wastar([h3,h4],w=2048,threshold=0.80,reopen_closed=false), lazy_wastar([h3,h4],w=1024,threshold=0.75,reopen_closed=false), lazy_wastar([h3,h4],w=512,threshold=0.70,reopen_closed=false),lazy_wastar([h3,h4],w=256,threshold=0.67,reopen_closed=false), lazy_wastar([h3,h4],w=128,threshold=0.65,reopen_closed=false), lazy_wastar([h3,h4],w=64,threshold=0.60,reopen_closed=false),lazy_wastar([h3,h4],w=32,threshold=0.58,reopen_closed=false), lazy_wastar([h3,h4],w=16,threshold=0.56,reopen_closed=false), lazy_wastar([h3,h4],w=8,threshold=0.54,reopen_closed=false),lazy_wastar([h3,h4],w=4,threshold=0.52,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.50,reopen_closed=false), lazy_wastar([h3,h4],w=1,threshold=0.49,reopen_closed=false)], continue_on_fail=true)"],

        "iterated_wa_2": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=false)], continue_on_fail=true)"],

        "iterated_wa_3": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.8,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=true)], continue_on_fail=true)"],

        "iterated_wa_4": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.8,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.7,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=true)], continue_on_fail=true)"],

        "iterated_wa_5": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=false)], continue_on_fail=true)"],

        "iterated_wa_6": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=1,threshold=0.6,reopen_closed=false)], continue_on_fail=true)"],
    }

def apl_configs_satisficing_extended():
    configs = {}
    configs.update(configs_satisficing_extended())
    return configs

def apl_satisficing_with_threshold():
    configs = {}
    configs.update(configs_satisficing_with_threshold())
    return configs


