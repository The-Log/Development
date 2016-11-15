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
  ifstream inFile ("/Users/ankurM/Development/cv/labs/edge_detection/image2.ppm");
  ofstream monoFile ("/Users/ankurM/Development/cv/labs/edge_detection/edgy2.ppm");
  getline (inFile,line);
  monoFile << line << " " << endl;

  getline (inFile,line);
  istringstream iss(line);
  int imageWidth, imageHeight;
  iss >> imageWidth, imageHeight;
  monoFile << line << " " << endl;

  getline (inFile,line);
  monoFile << line << endl;
  vector<vector<int> > vect(imageHeight, vector<int>(imageWidth));
  if (inFile.is_open())
  {
    while (getline (inFile, line))
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
        int max = std::max(std::max(a,b),c);
        int min = std::min(std::min(a,b),c);
        int avg = (min + max) / 2 ;
        //if(avg < 125)
        monoFile << avg << " " << avg << " " << avg << " ";
        //else
          //monoFile << 255 << " " << 255 << " " << 255 << " ";
      }
      monoFile << "\n";
    }
  }
  else{
    cout << "Unable to open file";
    return 0;
  }
  return 0;
}
