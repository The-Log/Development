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

int iterate(int** m, int dim){
  int max_dist = 0;
  int max_r = -1;
  int max_c = -1;

  for (int i=0; i<dim; i++){
    for (int j=0; j<dim;j++){
      if(m[i][j]==1 && i+j > max_dist){
        max_dist = i+j;
        max_r = i;
        max_c = j;
      }
    }
  }

  for (int i=0; i <=max_r; i++){
    for (int j=0; j<=max_c; j++){
      m[i][j]=1-m[i][j];
    }
  }
  return max_r == -1;
}
void printMatrix(int** m, int dim){
  for (int i=0; i < dim; i++){
    for (int j=0; j< dim; j++){
      std::cout << m[i][j];
    }
    std::cout << '\n';
  }
}
int main() {
  string line, s;
  ifstream myFile ("cowtip.in");
  ofstream outFile("cowtip.out");
  map<string, int> map;
  getline (myFile, line);
  int dim = std::stoi(line);
  int m[dim][dim];
  int i = 0;
  if (myFile.is_open())
  {
    while (getline (myFile, line)){
      int j = 0;
      for (char & c : line){
        m[i][j] = std::stoi(s + c);
        j++;
      }
      i++;
    }
  }
  int tally=0;
  bool done = false;


  int edim = dim;
  while (!done) {
    int max_dist = 0;
    int max_r = -1;
    int max_c = -1;
    for (int i=0; i<dim; i++){
      for (int j=0; j<dim;j++){
        // if(m[i][j]==1 && i+j > max_dist){
        if (m[i][j]==1 && (i > max_r || j > max_c)){
          max_dist = i+j;
          max_r = i;
          max_c = j;
        }
      }
    }

    for (int i=0; i <=max_r; i++){
      for (int j=0; j<=max_c; j++){
        m[i][j]=1-m[i][j];
      }
    }
    done = max_r == -1;
   for (int i=0; i < dim; i++){
     for (int j=0; j< dim; j++){
       std::cout << m[i][j];
     }
     std::cout << '\n';
  }
  std::cout << '\n';

    tally ++;
  }
  cout << tally-1;
  outFile << tally-1;
  return 0;
}
