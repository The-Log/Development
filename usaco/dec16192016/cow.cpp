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
  ifstream myFile ("cowsignal.in");
  ofstream outFile("cowsignal.out");
  getline (myFile,line);
  vector<string> tokens = split(line, ' ');
  int d = std::stoi(tokens[2]);
  if (myFile.is_open())
  {
    while (getline (myFile, line))
    {
      for (char & c : line){
        int j = 0;
        while(j < d){
          l = l + c;
          j++;
        }
      }
      int i = 0;
      while (i < d){
        outFile << l << '\n';
        i++;
      }
      l = "";
    }
  }
  return 0;
}
