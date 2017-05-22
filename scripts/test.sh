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

## Heuristics

MY_H="my_heuristic(tz_first = 203304688, tz_second = 320934904 )"
#admissible
BLIND_H="blind()"
LMCOUNT_A_H="lmcount(lm_hm(m=2),admissible=true)"
MERGE_H="merge_and_shrink(shrink_strategy=shrink_bisimulation(greedy=false),merge_strategy=merge_stateless(merge_selector=score_based_filtering(scoring_functions=[goal_relevance,dfp,total_order])),label_reduction=exact(before_shrinking=true,before_merging=false),max_states=50000,threshold_before_merge=1)"
CPDB_H="cpdbs(genetic(pdb_max_size=50000, num_collections=5, num_episodes=10, mutation_probability=0.01, disjoint=false, random_seed=-1))"
IPDB_H="ipdb()"
#not admissible
FF_H="ff()"
GC_H="goalcount()"
ADD_H="add()"
HM_H="hm()"
LMCUT_H="lmcut()"
LMCOUNT_H="lmcount(lm_hm(m=1))"
PDB_H="pdb(patterns=[[1,2],[3]])"
LMCOUNT_H="lmcount(lm_hm(m=2))"
MAX_H="hmax()"
#systematic(pattern_max_size=3, only_interesting_patterns=true)
../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$LMCOUNT_A_H, $BLIND_H]),reopen_closed=true,max_time=10)" >out.out 2>&1
./cat_db.sh
../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$MERGE_H, $IPDB_H]),reopen_closed=true,max_time=10)"  >>out.out 2>&1
./cat_db.sh
../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$CPDB_H, $LMCUT_H]),reopen_closed=true,max_time=10)"  >>out.out 2>&1
./cat_db.sh
../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar([$MY_H],w=2,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$MY_H]),reopen_closed=true,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([single($MY_H),single($FF_H)]),reopen_closed=true,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar([$MY_H, $FF_H],w=2,max_time=20)"

#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar($MY_H,w=2,max_time=120)"
#../fast-downward/fast-downward.py $HIKING_DOM $HIKING_PROB2 --search "lazy(tiebreaking([$LMCOUNT_H,$FF_H]),max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([single($ADD_H),single($FF_H)]),reopen_closed=true,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar([$MY_H],w=2,max_time=20)"
