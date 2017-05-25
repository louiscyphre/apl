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

MYdb_H="my_heuristic(tz_first = 203304688, tz_second = 320934904 , use_hdb=true, hdb_file_path=../scripts/db.ssv)"
#admissible
BLIND_H="blind()"
LMCOUNT_A_H="lmcount(lm_hm(m=2),admissible=true)"
MERGE_H="merge_and_shrink(shrink_strategy=shrink_bisimulation(greedy=false),merge_strategy=merge_stateless(merge_selector=score_based_filtering(scoring_functions=[goal_relevance,dfp,total_order])),label_reduction=exact(before_shrinking=true,before_merging=false),max_states=50000,threshold_before_merge=1)"
CPDB_H="cpdbs(genetic(pdb_max_size=50000, num_collections=5, num_episodes=10, mutation_probability=0.01, disjoint=false, random_seed=-1))"
IPDB_H="ipdb()"
#admissible db
BLINDdb_H="blind(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
LMCOUNTdb_A_H="lmcount(lm_hm(m=2),admissible=true, use_hdb=true, hdb_file_path=../scripts/db.ssv)"
MERGEdb_H="merge_and_shrink(shrink_strategy=shrink_bisimulation(greedy=false),merge_strategy=merge_stateless(merge_selector=score_based_filtering(scoring_functions=[goal_relevance,dfp,total_order])),label_reduction=exact(before_shrinking=true,before_merging=false),max_states=50000,threshold_before_merge=1, use_hdb=true, hdb_file_path=../scripts/db.ssv)"
CPDBdb_H="cpdbs(genetic(pdb_max_size=50000, num_collections=5, num_episodes=10, mutation_probability=0.01, disjoint=false, random_seed=-1), use_hdb=true, hdb_file_path=../scripts/db.ssv)"
IPDBdb_H="ipdb(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
#not admissible
FF_H="ff()"
GC_H="goalcount()"
ADD_H="add()"
HM_H="hm()"
LMCUT_H="lmcut()"
LMCOUNT_H="lmcount(lm_hm(m=2))"
MAX_H="hmax()"
#not admissible db
FFdb_H="ff(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
GCdb_H="goalcount(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
ADDdb_H="add(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
HMdb_H="hm(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
LMCUTdb_H="lmcut(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
LMCOUNTdb_H="lmcount(lm_hm(m=2),use_hdb=true, hdb_file_path=../scripts/db.ssv)"
MAXdb_H="hmax(use_hdb=true, hdb_file_path=../scripts/db.ssv)"
#systematic(pattern_max_size=3, only_interesting_patterns=true)
../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB2 --search "iterated([lazy(tiebreaking([$LMCOUNTdb_A_H, $BLINDdb_H]),max_time=120), lazy(tiebreaking([$MRGEdb_H $IPDBdb_H]),max_time=60), lazy(tiebreaking([$CPDBdb_H, $LMCUTdb_H]),max_time=30), lazy_wastar([$MYdb_H, $FFdb_H],w=3,max_time=20)], continue_on_fail=true, continue_on_solve=true)"

#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --heuristic "mer=$MERGEdb_H, ff=$FFdb_H, gc=$GCdb_H, add=$ADDdb_H, hm=$HMdb_H, lmcut=$LMCUTdb_H, lmc=$LMCOUNTdb_A_H, cpdb=$CPDBdb_H, max=$MAXdb_H, my=$MYdb_H, bli=$BLINDdb_H" --search "iterated([tiebreaking([lmc, bli],w=10,max_time=30),tiebreaking([mer, ipdb],w=5,max_time=20), tiebreaking([cpdb, lmcut],w=4,max_time=20), lazy_wastar([my, ff],w=3,max_time=20)])"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$LMCOUNT_A_H, $BLIND_H]),reopen_closed=true,max_time=20)" >out.out 2>&1
#./cat_db.sh
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$MERGE_H, $IPDB_H]),reopen_closed=true,max_time=10)"  >>out.out 2>&1
#./cat_db.sh
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$CPDB_H, $LMCUT_H]),reopen_closed=true,max_time=10)"  >>out.out 2>&1
#cat out.out | uniq > afb674ae56bc
#cat ./afb674ae56bc > out.out
#rm -f ./afb674ae56bc
#./cat_db.sh
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar([$MY_H, $FF_H],w=2,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(tiebreaking([$MY_H]),reopen_closed=true,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([single($MY_H),single($FF_H)]),reopen_closed=true,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar([$MY_H, $FF_H],w=2,max_time=20)"

#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar($MY_H,w=2,max_time=120)"
#../fast-downward/fast-downward.py $HIKING_DOM $HIKING_PROB2 --search "lazy(tiebreaking([$LMCOUNT_H,$FF_H]),max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([single($ADD_H),single($FF_H)]),reopen_closed=true,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar([$MY_H],w=2,max_time=20)"
