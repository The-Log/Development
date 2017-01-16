#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>

using namespace std;

vector<string> split(string str, char delimiter) {
  vector<string> s;
  stringstream ss(str);
  string tok;

  while(getline(ss, tok, delimiter)) {
    s.push_back(tok);
  }

  return s;
}

int main() {
  string line;
  ifstream myFile ("notlast.in");
  ofstream outFile("notlast.out");
  map<string, int> map;
  std::vector<string> names{"Bessie", "Elsie", "Daisy", "Gertie", "Annabelle", "Maggie", "Henrietta"};
  for (size_t i = 0; i < names.size(); i++) {
    map[names[i]] = 0;
  }
  getline (myFile, line);
  if (myFile.is_open())
  {
    while (getline (myFile, line)){
      vector<string> tokens = split(line, ' ');
      map[tokens.at(0)] = std::stoi(tokens.at(1)) + map[tokens.at(0)];
    }
  }
  string minname = "Tie";
  string min2name = "Tie";
  int min = std::numeric_limits<int>::max();
  int min2 = min;
  for (auto const& x : map){
    std::cout << x.first << " " <<  x.second << '\n';
    if (x.second < min){
      min2 = min;
      min2name = minname;
      min = x.second;
      minname = x.first;
    }
    else if (x.second == min){
      min = x.second;
      minname = x.first;
    }
    else if(x.second < min2){
      min2name = x.first;
      min2 = x.second;
    }
    else if(x.second == min2){
      min2name = "Tie";
    }
  }
  std::cout << min2name << '\n';
  outFile << min2name << endl;
  return 0;
}
