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
  ifstream myFile ("square.in");
  ofstream outFile("square.out");
  getline (myFile,line);
  vector<string> tokens1 = split(line, ' ');
  getline (myFile,line);
  vector<string> tokens2 = split(line, ' ');
  vector<int> xs;
  xs.push_back(std::stoi(tokens1[0])); xs.push_back(std::stoi(tokens1[2])); xs.push_back(std::stoi(tokens2[0])); xs.push_back(std::stoi(tokens2[2]));
  vector<int> ys;
  ys.push_back(std::stoi(tokens1[1])); ys.push_back(std::stoi(tokens1[3])); ys.push_back(std::stoi(tokens2[1])); ys.push_back(std::stoi(tokens2[3]));

  int minX = 9999; int maxX = -9999;
  for (int i = 0; i < xs.size() ; i++) {
    if(xs.at(i) > maxX)
      maxX = xs.at(i);
    if(xs.at(i) < minX)
      minX = xs.at(i);
  }
  int difx = maxX - minX;
  int miny = 9999; int maxy = -9999;
  for (int i = 0; i < ys.size() ; i++) {
    if(ys.at(i) > maxy)
      maxy = ys.at(i);
    if(ys.at(i) < miny)
      miny = ys.at(i);
  }
  int dify = maxy - miny;
  int m = max(difx,dify);
  outFile << m * m << '\n';
  return 0;
}
