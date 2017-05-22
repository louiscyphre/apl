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

## Heuristics

MAX_H="hmax()"
FF_H="ff()"
GC_H="goalcount()"
IPDB_H="ipdb()"
ADD_H="add()"
MY_H="my_heuristic(tz_first = 203304688, tz_second = 320934904 )"
BLIND_H="blind()"
HM_H="hm()"
LMCUT_H="lmcut()"
PDB_H="pdb(patterns=[[1,2],[3]])"
LMCOUNT_H="lmcount(lm_hm(m=1))"
CPDB_H="cpdbs(systematic(pattern_max_size=1, only_interesting_patterns=true))"
#systematic(pattern_max_size=3, only_interesting_patterns=true)
#genetic(pdb_max_size=50000, num_collections=5, num_episodes=10, mutation_probability=0.01, disjoint=false, random_seed=-1)


../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(single(sum($GC_H,g())),max_time=120)"
#../fast-downward/fast-downward.py $BARMAN_DOM $BARMAN_PROB2 --search "lazy(alt([tiebreaking([$LMCOUNT_H,$FF_H]),tiebreaking([$CPDB_H,sum($GC_H,g())])]),max_time=120)"
#../fast-downward/fast-downward.py $TETRIS_DOM $TETRIS_PROB --search "lazy(alt([tiebreaking([$LMCOUNT_H,$FF_H]),tiebreaking([$FF_H,sum($GC_H,g())])]),max_time=120)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar($MY_H,w=2,max_time=120)"
#../fast-downward/fast-downward.py $HIKING_DOM $HIKING_PROB2 --search "lazy(tiebreaking([$LMCOUNT_H,$FF_H]),max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy(alt([single($ADD_H),single($FF_H)]),reopen_closed=true,max_time=20)"
#../fast-downward/fast-downward.py $PUZZLE_DOM $PUZZLE_PROB1 --search "lazy_wastar([$MY_H],w=2,max_time=20)"
