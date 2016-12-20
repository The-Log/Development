#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

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
  string s, l;
  ifstream myFile ("blocks.in");
  ofstream outFile("blocks.out");
  std::vector<int> v;
  getline (myFile,line);
  if (myFile.is_open())
  {
    while (getline (myFile, line)){
      vector<string> tokens = split(line, ' ');
      std::set<string> visited;
      for (char & c : tokens[1]){
        
      }
    }
  }
  return 0;
}
