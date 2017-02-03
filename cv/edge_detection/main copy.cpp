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
  ifstream inFile1 ("/Users/ankurM/Development/cv/labs/edge_detection/image.ppm");
  ofstream edgyFile ("/Users/ankurM/Development/cv/labs/edge_detection/edgy.ppm");
  getline (inFile1,line);
  edgyFile << line << " " << endl;

  getline (inFile1,line);
  vector<string> tokens = split(line, ' ');
  int imageWidth = std::stoi(tokens[0]); int imageHeight = std::stoi(tokens[1]);
  Matrix m = Matrix(imageWidth * 3, imageHeight);
  edgyFile << line << " " << endl;

  getline (inFile1,line);
  edgyFile << line << endl;

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
        int sum = a + b + c;
        double avg = sum / 3.0 ;

        if(avg < 127.5){
          array.push_back(0);
        }
        else {
          array.push_back(255);
        }
      }
    }
    //std::cout << "GOT HERE" << std::endl;
  }
  else{
    cout << "Unable to open file";
    return 0;
  }

  for (int i = 0; i < imageWidth - 2; i++) {
    for (int j = 0; j < imageHeight; j++) {
      m(i,j) = array.at(i * imageHeight + j);
      m(i + 1,j) = array.at(i / 3 * imageHeight + j);
      m(i + 2,j) = array.at(i / 3 * imageHeight + j);
    }
  }
  Matrix m1 = m; //Matrix(imageWidth * 3, imageHeight);
  for (int i = 0; i < m1.r; i++) {
    for (int j = 0; j < m1.c; j++) {
      //m1(i,j) = m(i,j);
      if(m(i,j) == 255){
        if(i + 1 < m1.r && j + 1 < m1.c){
          m1(i, j + 1) = 255;
          m1(i + 1, j) = 255;
          m1(i + 1,j + 1) = 255;
        }
        if(i - 1 > 0 && j + 1 < m1.c ){
          m1(i - 1,j + 1) = 255;
        }
        if(i + 1 < m1.r && j - 1 > 0){
          m1(i + 1,j - 1) = 255;
        }
        if(i - 1 > 0 && j - 1 > 0 ){
          m1(i, j - 1) = 255;
          m1(i - 1, j) = 255;
          m1(i - 1,j - 1) = 255;
        }
      }
    }
  }
  //m1.display();
  for (int i = 0; i < m.r; i++) {
    for (int j = 0; j < m.c; j++) {
      //edgyFile << m1(i,j) << " " << m1(i,j) << " " << m1(i,j) << " ";
      edgyFile << m1(i,j) - m(i,j) << " " << m1(i,j) - m(i,j) << " " << m1(i,j) - m(i,j) << " ";
    }
    edgyFile << std::endl;
  }
  return 0;
}
