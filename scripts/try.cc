#include <iostream>
#include<boost/functional/hash.hpp>
#include <string>
#include <vector>
#include<unordered_map>
#include<algorithm>
#include<fstream>
using namespace std;

int main()
{
    string key; string value;
    fstream f;
    std::unordered_map<long,int> m;
    m[666] = 10;
    for( auto it : m )
        m[ it.first ] += 50;
    cout << to_string( m[666] ) <<endl;

}
