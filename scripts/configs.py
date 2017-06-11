
def configs_satisficing_with_threshold_better():
    return {
        "iterated_best_threshold_better": [
        "--heuristic",
        "h1=lmcount(lm_factory=lm_rhw(lm_cost_type=ONE),pref=true)",
        "--heuristic",
        "h2=ff()",
        "--heuristic",
        "h3=goalcount()",
        "--heuristic",
        "h4=ipdb(max_time=40)",
        "--search",
        "iterated([lazy(alt([tiebreaking([h1,h2]),tiebreaking([h1,h3]),tiebreaking([h4,h2])]),preferred=[h1,h2],cost_type=ONE,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.9,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.8,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.7,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.6,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.5,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.4,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.3,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.2,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.1,max_time=1800),lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=PLUSONE,w=2,threshold=0,max_time=1800),],cost_type=ONE,continue_on_fail=true,repeat_last=true,max_time=1800)"]
}


def configs_satisficing_with_threshold():
    return {
        "iterated_best_threshold": [
        "--heuristic",
        "h1=lmcount(lm_factory=lm_rhw(lm_cost_type=ONE),pref=true)",
        "--heuristic",
        "h2=ff()",
        "--heuristic",
        "h3=goalcount()",
        "--heuristic",
        "h4=ipdb(max_time=40)",
        "--search",
        "iterated([lazy(alt([tiebreaking([h1,h2]),tiebreaking([h1,h3]),tiebreaking([h4,h2])]),preferred=[h1,h2],cost_type=ONE,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.9,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.8,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.7,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.6,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.3,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.2,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.1,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=2,threshold=0,max_time=1000)],pass_bound=true,continue_on_fail=true,continue_on_solve=true,max_time=1000)"]
    }

def configs_satisficing_no_threshold():
    return {
        "iterated_best_no_threshold": [
        "--heuristic",
        "h1=lmcount(lm_factory=lm_rhw(lm_cost_type=ONE),pref=true)",
        "--heuristic",
        "h2=ff()",
        "--heuristic",
        "h3=goalcount()",
        "--heuristic",
        "h4=ipdb(max_time=40)",
        "--search",
        "iterated([lazy(alt([tiebreaking([h1,h2]),tiebreaking([h1,h3]),tiebreaking([h4,h2])]),preferred=[h1,h2],cost_type=ONE,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=2,max_time=1000)],pass_bound=true,continue_on_fail=true,continue_on_solve=true,max_time=1000)"]
    }

def apl_satisficing_with_threshold():
    configs = {}
    configs.update(configs_satisficing_with_threshold())
    return configs

def apl_satisficing_with_threshold_better():
    configs = {}
    configs.update(configs_satisficing_with_threshold_better())
    return configs



def apl_satisficing_no_threshold():
    configs = {}
    configs.update(configs_satisficing_no_threshold())
    return configs
