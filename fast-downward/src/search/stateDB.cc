#include <fstream>
#include "stateDB.h"

StateDB::StateDB( const std::string dbfile ){
    fstream dbf;
    std::string key,value;

    dbf.open(dbfile,ios::in);
    while( dbf >> key >> value )
        database[ stoul(key) ] = stoi(value);
}

