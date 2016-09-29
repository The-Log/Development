#include <iostream>
#include <fstream>
#include <sstream>
#include "matrix.cpp"
#include <math.h>
#include <vector>

using namespace std;

Matrix setProjectionMatrix(const float &near, const float &far, Matrix m)
{
    float scale = 1 / tan(90 * 0.5 * 3.14 / 180);
    m(0,0) = scale;
    m(1,1) = scale;
    m(2,2) = -far / (far - near);
    m(3,2) = -far * near / (far - near);
    m(2,3) = -1;
    m(3,3) = 0;
    return m;
}

int main() {
  string line;
  ifstream myFile ("/Users/ankurM/Development/cv/labs/coordinates.txt");
  getline (myFile,line);
  istringstream iss(line);
  int size = 0; iss >> size;
  Matrix pm = Matrix(4,4);
  pm = setProjectionMatrix(0.1, 100,pm);
  vector<Matrix> arr;
  arr.reserve(size);
  int i = 0; int j = 0;
  if (myFile.is_open())
  {
    while (getline (myFile,line) )
    {
        Matrix m = Matrix(1, 4);
        int a, b, c;
        istringstream iss(line);
        iss >> a >> b >> c;
        m(0,j+1) =b;
        m(0,j+2) =c;
        m(0,j+3) = 1;
        arr.push_back(m);
        ++i;
    }
    myFile.close();
  }
  else{
    cout << "Unable to open file";
    return 0;
  }
  for (unsigned i=0; i<arr.size(); i++){
     arr.at(i) = arr.at(i) * pm ;
     arr.at(i).display();
  }
  return 0;
}
