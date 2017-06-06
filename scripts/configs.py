def configs_satisficing_with_threshold():
    return {
<<<<<<< HEAD
        "iterated_wa_0_lm1": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,threshold=0.98,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.95,reopen_closed=false), lazy_wastar([h3,h4],w=4,threshold=0.90,reopen_closed=false), lazy_wastar([h3,h4],w=8,threshold=0.85,reopen_closed=false),lazy_wastar([h3,h4],w=16,threshold=0.80,reopen_closed=false), lazy_wastar([h3,h4],w=32,threshold=0.75,reopen_closed=false), lazy_wastar([h3,h4],w=64,threshold=0.70,reopen_closed=false),lazy_wastar([h3,h4],w=128,threshold=0.67,reopen_closed=false), lazy_wastar([h3,h4],w=256,threshold=0.65,reopen_closed=false), lazy_wastar([h3,h4],w=512,threshold=0.60,reopen_closed=false),lazy_wastar([h3,h4],w=1024,threshold=0.58,reopen_closed=false), lazy_wastar([h3,h4],w=2048,threshold=0.56,reopen_closed=false), lazy_wastar([h3,h4],w=4096,threshold=0.54,reopen_closed=false),lazy_wastar([h3,h4],w=8192,threshold=0.52,reopen_closed=false), lazy_wastar([h3,h4],w=16384,threshold=0.50,reopen_closed=false), lazy_wastar([h3,h4],w=32768,threshold=0.49,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_0_inverted_weights_lm1": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=32768,threshold=0.98,reopen_closed=false), lazy_wastar([h3,h4],w=16384,threshold=0.95,reopen_closed=false), lazy_wastar([h3,h4],w=8192,threshold=0.90,reopen_closed=false), lazy_wastar([h3,h4],w=4096,threshold=0.85,reopen_closed=false),lazy_wastar([h3,h4],w=2048,threshold=0.80,reopen_closed=false), lazy_wastar([h3,h4],w=1024,threshold=0.75,reopen_closed=false), lazy_wastar([h3,h4],w=512,threshold=0.70,reopen_closed=false),lazy_wastar([h3,h4],w=256,threshold=0.67,reopen_closed=false), lazy_wastar([h3,h4],w=128,threshold=0.65,reopen_closed=false), lazy_wastar([h3,h4],w=64,threshold=0.60,reopen_closed=false),lazy_wastar([h3,h4],w=32,threshold=0.58,reopen_closed=false), lazy_wastar([h3,h4],w=16,threshold=0.56,reopen_closed=false), lazy_wastar([h3,h4],w=8,threshold=0.54,reopen_closed=false),lazy_wastar([h3,h4],w=4,threshold=0.52,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.50,reopen_closed=false), lazy_wastar([h3,h4],w=1,threshold=0.49,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_2": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_3": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.8,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=true)], continue_on_fail=true, continue_on_solve=true)"],

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
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.8,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.7,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=true)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_5": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_6": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=1,threshold=0.6,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_4_inverted_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.7,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.8,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=true)], continue_on_fail=true, continue_on_solve=true)"],

    }


def configs_satisficing_no_threshold():
    return {
        "iterated_wa_0_lm1_no_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=4,reopen_closed=false), lazy_wastar([h3,h4],w=8,reopen_closed=false), lazy_wastar([h3,h4],w=16,reopen_closed=false), lazy_wastar([h3,h4],w=32,reopen_closed=false), lazy_wastar([h3,h4],w=64,reopen_closed=false),lazy_wastar([h3,h4],w=128,reopen_closed=false), lazy_wastar([h3,h4],w=256,reopen_closed=false), lazy_wastar([h3,h4],w=512,reopen_closed=false), lazy_wastar([h3,h4],w=1024,reopen_closed=false), lazy_wastar([h3,h4],w=2048,reopen_closed=false), lazy_wastar([h3,h4],w=4096,reopen_closed=false),lazy_wastar([h3,h4],w=8192,reopen_closed=false), lazy_wastar([h3,h4],w=16384,reopen_closed=false), lazy_wastar([h3,h4],w=32768,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_0_inverted_weights_lm1_no_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=32768,reopen_closed=false), lazy_wastar([h3,h4],w=16384,reopen_closed=false), lazy_wastar([h3,h4],w=8192,reopen_closed=false), lazy_wastar([h3,h4],w=4096,reopen_closed=false),lazy_wastar([h3,h4],w=2048,reopen_closed=false), lazy_wastar([h3,h4],w=1024,reopen_closed=false), lazy_wastar([h3,h4],w=512,reopen_closed=false),lazy_wastar([h3,h4],w=256,reopen_closed=false), lazy_wastar([h3,h4],w=128,reopen_closed=false), lazy_wastar([h3,h4],w=64,reopen_closed=false),lazy_wastar([h3,h4],w=32,reopen_closed=false), lazy_wastar([h3,h4],w=16,reopen_closed=false), lazy_wastar([h3,h4],w=8,reopen_closed=false),lazy_wastar([h3,h4],w=4,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=1,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_2_no_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_3_no_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=true)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_4_no_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=true)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_5_no_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,reopen_closed=false), lazy_wastar([h3,h4],w=2,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_6_no_threshold": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,reopen_closed=false), lazy_wastar([h3,h4],w=1,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],
    }


def configs_satisficing_with_threshold_bad():
    return {
        "iterated_wa_0_lm1": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=1))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=1),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,threshold=0.98,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.95,reopen_closed=false), lazy_wastar([h3,h4],w=4,threshold=0.90,reopen_closed=false), lazy_wastar([h3,h4],w=8,threshold=0.85,reopen_closed=false),lazy_wastar([h3,h4],w=16,threshold=0.80,reopen_closed=false), lazy_wastar([h3,h4],w=32,threshold=0.75,reopen_closed=false), lazy_wastar([h3,h4],w=64,threshold=0.70,reopen_closed=false),lazy_wastar([h3,h4],w=128,threshold=0.67,reopen_closed=false), lazy_wastar([h3,h4],w=256,threshold=0.65,reopen_closed=false), lazy_wastar([h3,h4],w=512,threshold=0.60,reopen_closed=false),lazy_wastar([h3,h4],w=1024,threshold=0.58,reopen_closed=false), lazy_wastar([h3,h4],w=2048,threshold=0.56,reopen_closed=false), lazy_wastar([h3,h4],w=4096,threshold=0.54,reopen_closed=false),lazy_wastar([h3,h4],w=8192,threshold=0.52,reopen_closed=false), lazy_wastar([h3,h4],w=16384,threshold=0.50,reopen_closed=false), lazy_wastar([h3,h4],w=32768,threshold=0.49,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],
        "iterated_wa_0_lm2": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=1,threshold=0.98,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.95,reopen_closed=false), lazy_wastar([h3,h4],w=4,threshold=0.90,reopen_closed=false), lazy_wastar([h3,h4],w=8,threshold=0.85,reopen_closed=false),lazy_wastar([h3,h4],w=16,threshold=0.80,reopen_closed=false), lazy_wastar([h3,h4],w=32,threshold=0.75,reopen_closed=false), lazy_wastar([h3,h4],w=64,threshold=0.70,reopen_closed=false),lazy_wastar([h3,h4],w=128,threshold=0.67,reopen_closed=false), lazy_wastar([h3,h4],w=256,threshold=0.65,reopen_closed=false), lazy_wastar([h3,h4],w=512,threshold=0.60,reopen_closed=false),lazy_wastar([h3,h4],w=1024,threshold=0.58,reopen_closed=false), lazy_wastar([h3,h4],w=2048,threshold=0.56,reopen_closed=false), lazy_wastar([h3,h4],w=4096,threshold=0.54,reopen_closed=false),lazy_wastar([h3,h4],w=8192,threshold=0.52,reopen_closed=false), lazy_wastar([h3,h4],w=16384,threshold=0.50,reopen_closed=false), lazy_wastar([h3,h4],w=32768,threshold=0.49,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_0_inverted_weights_lm2": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=32768,threshold=0.98,reopen_closed=false), lazy_wastar([h3,h4],w=16384,threshold=0.95,reopen_closed=false), lazy_wastar([h3,h4],w=8192,threshold=0.90,reopen_closed=false), lazy_wastar([h3,h4],w=4096,threshold=0.85,reopen_closed=false),lazy_wastar([h3,h4],w=2048,threshold=0.80,reopen_closed=false), lazy_wastar([h3,h4],w=1024,threshold=0.75,reopen_closed=false), lazy_wastar([h3,h4],w=512,threshold=0.70,reopen_closed=false),lazy_wastar([h3,h4],w=256,threshold=0.67,reopen_closed=false), lazy_wastar([h3,h4],w=128,threshold=0.65,reopen_closed=false), lazy_wastar([h3,h4],w=64,threshold=0.60,reopen_closed=false),lazy_wastar([h3,h4],w=32,threshold=0.58,reopen_closed=false), lazy_wastar([h3,h4],w=16,threshold=0.56,reopen_closed=false), lazy_wastar([h3,h4],w=8,threshold=0.54,reopen_closed=false),lazy_wastar([h3,h4],w=4,threshold=0.52,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.50,reopen_closed=false), lazy_wastar([h3,h4],w=1,threshold=0.49,reopen_closed=false)], continue_on_fail=true, continue_on_solve=true)"],

        "iterated_wa_4_lm2": [
            "--heuristic",
            "h1=lmcount(lm_hm(m=2))",
            "--heuristic",
            "h2=ff()",
            "--heuristic",
            "h3=lmcount(lm_hm(m=2),admissible=true)",
            "--heuristic",
            "h4=hmax()",
            "--search",
            "iterated([lazy(tiebreaking([h1,h2]),preferred=[h1,h2]), lazy_wastar([h3,h4],w=2,threshold=0.9,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.8,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.7,reopen_closed=false), lazy_wastar([h3,h4],w=2,threshold=0.6,reopen_closed=true)], continue_on_fail=true, continue_on_solve=true)"],
    }


def apl_configs_satisficing_extended():
    configs = {}
    configs.update(configs_satisficing_extended())
    return configs

def apl_configs_satisficing_ipc_no_threshold():
    configs = {}
    configs.update(configs_satisficing_ipc())
    return configs

def apl_satisficing():
=======
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
        "iterated([lazy(alt([tiebreaking([h1,h2]),tiebreaking([h1,h3]),tiebreaking([h4,h2])]),preferred=[h1,h2],cost_type=ONE,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.9,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.8,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.7,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.6,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,threshold=0.5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.3,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.2,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,threshold=0.1,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=2,threshold=0,max_time=1000)],pass_bound=true,continue_on_fail=true,continue_on_solve=true,max_time=1000)"
    }

def configs_satisficing_no_threshold():
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
        "iterated([lazy(alt([tiebreaking([h1,h2]),tiebreaking([h1,h3]),tiebreaking([h4,h2])]),preferred=[h1,h2],cost_type=ONE,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=4,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=5,max_time=1000), lazy_wastar([h1,h2,h4],preferred=[h1,h2],cost_type=ONE,w=2,max_time=1000)],pass_bound=true,continue_on_fail=true,continue_on_solve=true,max_time=1000)"
    }

def apl_satisficing_with_threshold():
>>>>>>> 5732f2ff3204a39b14ed492231fc1c663892dc9b
    configs = {}
    configs.update(configs_satisficing_with_threshold())
    configs.update(configs_satisficing_no_threshold())
    return configs


def apl_satisficing_no_threshold():
    configs = {}
    configs.update(configs_no_threshold())
    return configs
   
