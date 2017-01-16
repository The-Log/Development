#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cstring>

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
  ifstream myFile ("hps.in");
  ofstream outFile("hps.out");
  getline (myFile,line);
  int m[4][4];
  for (size_t i = 0; i < 4; i++)
    for (size_t j = 0; j < 4; j++)
      m[i][j]=0;
  if (myFile.is_open())
  {
    while (getline (myFile, line)){
      vector<string> tokens = split(line, ' ');
      int x = std::stoi(tokens.at(0));
      int y = std::stoi(tokens.at(1));
      m[x][y]++;
    }
  }
  outFile << max(m[1][2]+m[2][3]+m[3][1], m[2][1]+m[3][2]+m[1][3]);
  return 0;
}
