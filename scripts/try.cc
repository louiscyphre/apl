#include <iostream>
#include<boost/functional/hash.hpp>
#include <string>
#include <vector>
#include<unordered_map>
#include<algorithm>
#include<fstream>
#include<iterator>
using namespace std;

int main()
{
    vector<string> vec;
    vector<string>::iterator it;
    vec.push_back("666");
    vec.push_back("1666");
    vec.push_back("16666");
    it = vec.begin();
    std::cout<< *it <<std::endl;
    std::cout<< *++it <<std::endl;
}
