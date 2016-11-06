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
  ifstream inFile1 ("/Users/ankurM/Development/cv/labs/edge_detection/image.ppm");
  ofstream outFile2 ("/Users/ankurM/Development/cv/labs/edge_detection/edgy.ppm");
  getline (inFile1,line);
  outFile2 << line << " " << endl;
  getline (inFile1,line);
  istringstream iss(line);
  int imageWidth, imageHeight;
  iss >> imageWidth, imageHeight;
  outFile2 << line << " " << endl;
  getline (inFile1,line);
  outFile2 << line << endl;
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
        int max = std::max(std::max(a,b),c);
        int min = std::min(std::min(a,b),c);
        int avg = (min + max) / 2 ;
        if(avg > 125)
          outFile2 << 0 << " " << 0 << " " << 0 << " ";
        else
          outFile2 << 255 << " " << 255 << " " << 255 << " ";
      }
      outFile2 << "\n";
    }
  }
  else{
    cout << "Unable to open file";
    return 0;
  }
  return 0;
}
