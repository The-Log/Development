#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <string>

using namespace std;

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
      line.erase( remove( line.begin(), line.end(), ' ' ), line.end() );

      int i = 0;
      while(i < line.size() - 1){
        string s1(1, line[i]);
        if(i == line.size() - 2)
          std::cout << s1 << std::endl;
        a = std::stoi(s1);
        i ++;
        string s2(1, line[i]);
        b = std::stoi(s2);
        i ++;
        string s3(1, line[i]);
        c = std::stoi(s3);
        //outFile2 << a << " " << b << " " << c << " ";
        i ++;
        int max = std::max(std::max(a,b),c);
        int min = std::min(std::min(a,b),c);
        int avg = (min + max) / 2 ;
        outFile2 << avg << " " << avg << " " << avg << " ";
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
