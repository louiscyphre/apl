#!/bin/bash


## Domains and problems

PUZZLE_DOM=../problems/tile/domain.pddl
PUZZLE_PROB1=../problems/tile/puzzle01.pddl
PUZZLE_PROB2=../problems/tile/puzzle02.pddl
PUZZLE_RLX=../problems/tile/puzzle_rlx.pddl

KNIGHTS_DOM=../problems/knights_tour/knights_tour.pddl
KNIGHTS_PROB1=../problems/knights_tour/knights_tour5.pddl
KNIGHTS_PROB2=../problems/knights_tour/knights_tour8.pddl

HIKING_DOM=../problems/Hiking/domain.pddl
HIKING_PROB1=../problems/Hiking/ptesting-3-4-6.pddl
HIKING_PROB2=../problems/Hiking/ptesting-3-4-7.pddl
HIKING_PROB3=../problems/Hiking/ptesting-3-4-8.pddl

TETRIS_DOM=../problems/downward-benchmarks/tetris-sat14-strips/domain.pddl
TETRIS_PROB=../problems/downward-benchmarks/tetris-sat14-strips/p020.pddl

BARMAN_DOM=../problems/downward-benchmarks/barman-sat11-strips/domain.pddl 
BARMAN_PROB1=../problems/downward-benchmarks/barman-sat11-strips/pfile06-021.pddl
BARMAN_PROB2=../problems/downward-benchmarks/barman-sat11-strips/pfile10-039.pddl

GRIPPER_DOM=../problems/downward-benchmarks/gripper/domain.pddl
GRIPPER_PROB1=../problems/downward-benchmarks/gripper/prob20.pddl

# It took 1644 seconds to solve this problem and the solution was 2197(costs), or 187 steps.
TRANSP_DOM=../problems/downward-benchmarks/transport-sat11-strips/domain.pddl
TRANSP_PROB=../problems/downward-benchmarks/transport-sat11-strips/p01.pddl

# 84 seconds, cost 343, length 163
BARMAN_DOM=../problems/downward-benchmarks/barman-sat11-strips/domain.pddl
BARMAN_PROB=../problems/downward-benchmarks/barman-sat11-strips/pfile08-030.pddl

## Heuristics
W=2
MAX_H="hmax()"
FF_H="ff()"
GC_H="goalcount()"
IPDB_H="ipdb(max_time=10,cache_estimates=false,num_samples=500,collection_max_size=2000000,pdb_max_size=200000)"
ADD_H="add()"
MY_H="my_heuristic(tz_first = 203304688, tz_second = 320934904 )"
BLIND_H="blind()"
HM_H="hm()"
LMCUT_H="lmcut()"
PDB_H="pdb(patterns=[[1,2],[3]])"
LMCOUNT_H="lmcount(lm_rhw(),pref=true)"
CPDB_H="cpdbs(systematic())"
#genetic()


../fast-downward/fast-downward.py $TRANSP_DOM $TRANSP_PROB --heuristic h1=$LMCUT_H --heuristic h2=$FF_H --search "eager(tiebreaking([h1,h2]),reopen_closed=true,preferred=[h2],bound=20000,max_time=60)"


# VERY GOOD FOR HARD PROBLEMS:
#this one tool 1950 seconds with price 2350
#../fast-downward/fast-downward.py $TRANSP_DOM $TRANSP_PROB --heuristic h1=$LMCOUNT_H --heuristic h2=$FF_H --heuristic h3=$ADD_H --search "lazy(tiebreaking([h1,h2,h3]),preferred=[h1,h2],cost_type=ONE,max_time=3600)"

#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([single($CPDB_H),single($LMCOUNT_H),single($FF_H),single($IPDB_H),single($LMCUT_H)]),max_time=120)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar($MY_H,w=1,max_time=120)"

#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([tiebreaking(sum(g())])   (sum([$MY_H,$]))]),max_time=120)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([tiebreaking([$LMCOUNT_H,$FF_H]),tiebreaking([$CPDB_H,sum($GC_H,g())])]),max_time=120)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([tiebreaking([$LMCOUNT_H,$FF_H]),tiebreaking([$FF_H,sum($GC_H,g())])]),max_time=120)"
#../fast-downward/fast-downward.py $BARMAN_DOM $BARMAN_PROB2 --search "lazy(alt([tiebreaking([$LMCOUNT_H,$FF_H]),tiebreaking([$CPDB_H,sum($GC_H,g())])]),max_time=120)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "iterated([lazy(tiebreaking([$LMCOUNT_H,$ADD_H,$GC_H])),lazy_wastar($FF_H,w=2)],max_time=120)"
