#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include "matrix.cpp"

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
  ifstream inFile1 ("/Users/ankurM/Development/cv/labs/edge_detection/image3.ppm");
  ofstream edgyFile ("/Users/ankurM/Development/cv/labs/edge_detection/edgy.ppm");
  getline (inFile1,line);
  edgyFile << line << " " << endl;

  getline (inFile1,line);
  vector<string> tokens = split(line, ' ');
  int imageWidth = std::stoi(tokens[0]); int imageHeight = std::stoi(tokens[1]);
  Matrix m = Matrix(imageWidth, imageHeight);
  edgyFile << line << " " << endl;

  getline (inFile1,line);
  edgyFile << 1 << endl;

  vector<int> array;
  if (inFile1.is_open())
  {
    while (getline (inFile1, line))
    {
      int a, b, c;
      int i = 0;
      vector<string> tokens = split(line, ' ');
      while(i < tokens.size() - 2){
        a = std::stoi(tokens[i]);
        i ++;
        b = std::stoi(tokens[i]);
        i ++;
        c = std::stoi(tokens[i]);
        i ++;
        double avg = 0.3 * a + 0.59 * b + 0.11 * c; //0.30 * num[i] + 0.59 * num[i+1] + 0.11 * num[i+2
        //double avg = sum / 3.0 ;

        if(avg < 127.5 ){
          array.push_back(0);
        }
        else {
          array.push_back(1);
        }
      }
    }
  }
  else{
    cout << "Unable to open file";
    return 0;
  }
  Matrix m1 = Matrix(imageWidth, imageHeight);
  for (int i = 0; i < imageWidth; i++) {
    for (int j = 0; j < imageHeight; j++) {
      m(i,j) = array.at(i * imageHeight + j);
      m1(i,j) = 1;
    }
  }
  int dx[9] = {1,1,1,-1,-1,-1,0,0,0};
  int dy[9] = {0,1,-1,0,1,-1,1,-1,0};
  for (int i = 0; i < m1.r; i++) {
    for (int j = 0; j < m1.c; j++) {
      if(m(i,j) == 0) {
        for (int z = 0; z < 9; ++z) {
            if (i+dx[z] > -1 && i+dx[z]<m1.r && j+dy[z]>-1 && j+dy[z]<m1.c) {
              m1(i+dx[z],j+dy[z]) = 0;
            }
        }
      }
    }
  }
  m1(2,1) = 0;
  //m1.display();
  for (int i = 0; i < m.r; i++) {
    for (int j = 0; j < m.c; j++) {
      //edgyFile << m(i,j) << " " << m(i,j) << " " << m(i,j) << " ";
      //edgyFile << m1(i,j) - m(i,j) << " " << m1(i,j) - m(i,j) << " " << m1(i,j) - m(i,j) << " ";
      if (m1(i,j) == 0 && m(i,j) != 0) {
        edgyFile << " 0 0 0";
      } else {
        edgyFile << " 1 1 1";
      }
    }
    edgyFile << std::endl;
  }
  return 0;
}
