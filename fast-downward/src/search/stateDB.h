#include <unordered_map>
#include <string>
#include "../global_state.h"

class StateDB{

    std::unordered_map database;

    public:
        StateDB( const std::string dbfile );

        int get_h( GlobalState &state );
}
