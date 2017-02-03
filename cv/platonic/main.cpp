
#include <iostream>
#include <fstream>
#include <sstream>
#include "matrix.cpp"
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

Matrix multPointMatrix(Matrix in, Matrix M){
  Matrix out = Matrix(1, 4);
  out(0,0)  = in(0,0) * M(0,0) + in(0,1) * M(1,0) + in(0,2) * M(2,0) +  M(3,0);
  out(0,1)  = in(0,0) * M(0,1) + in(0,1) * M(1,1) + in(0,2) * M(2,1) +  M(3,1);
  out(0,2)  = in(0,0) * M(0,2) + in(0,1) * M(1,2) + in(0,2) * M(2,2) +  M(3,2);
  out(0,3)  = in(0,0) * M(0,3) + in(0,1) * M(1,3) + in(0,2) * M(2,3) +  M(3,3);
  float w = out(0,3);
  out(0,0) /= w;
  out(0,1) /= w;
  out(0,2) /= w;

  return out;
}
Matrix rmx(float angle){
  Matrix rm = Matrix(4, 4);
  rm(0,0) = 1;
  rm(1,1) = cos(angle);
  rm(1,2) = -sin(angle);
  rm(2,1) = sin(angle);
  rm(2,2) = cos(angle);
  rm(3,3) = 1;
  return rm;
}
Matrix rmy(float angle){
  Matrix rm = Matrix(4, 4);
  rm(0,0) = cos(angle);
  rm(0,2) = sin(angle);
  rm(1,1) = 1;
  rm(2,0) = -sin(angle);
  rm(2,2) = cos(angle);
  rm(3,3) = 1;
  return rm;
}
Matrix rmz(float angle){
  Matrix rm = Matrix(4, 4);
  rm(0,0) = cos(angle);
  rm(0,1) = -sin(angle);
  rm(1,0) = sin(angle);
  rm(1,1) = cos(angle);
  rm(2,2) = 1;
  rm(3,3) = 1;
  return rm;
}
Matrix setProjectionMatrix(const float &near, const float &far, Matrix m)
{
  float scale = 1 / tan(90 * 0.5 * M_PI / 180);
  m(0,0) = scale;
  m(1,1) = scale;
  m(2,2) = -far / (far - near);
  m(3,2) = -far * near / (far - near);
  m(2,3) = -1;
  m(3,3) = 0;
  return m;
}
Matrix setCamera(Matrix m)
{
  m(0,0) = 1;
  m(1,1) = 1;
  m(2,2) = 1;
  m(3,0) = 0;
  m(3,1) = 0;
  m(3,2) = -3; // zoom
  m(3,3) = 1;
  return m;
}

int main() {
  int imageWidth = 500;
  int imageHeight = 500;
  string line;
  ifstream myFile ("/Users/ankurM/Development/cv/labs/shapes/tetrahedron.txt");
  getline (myFile,line);
  istringstream iss(line);
  int size = 0; iss >> size;
  Matrix pm = Matrix(4,4);
  pm = setProjectionMatrix(0.1, 100, pm);
  Matrix shift = Matrix(4,4);
  shift = setCamera(shift);
  vector<Matrix> arr;
  arr.reserve(size);
  int i = 0; int j = 0;
  if (myFile.is_open())
  {
    while (getline (myFile,line) )
    {
      Matrix m = Matrix(1, 4);
      double a, b, c;
      istringstream iss(line);
      iss >> a >> b >> c;
      m(0,j) = a;
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
  vector<int> xco;
  vector<int> yco;
  for (unsigned i = 0; i<arr.size(); i++){
    Matrix temp = multPointMatrix(arr.at(i) , rmx(45));
    temp = multPointMatrix(temp, rmy(45));
    temp = multPointMatrix(temp, rmz(0));
    temp = multPointMatrix(temp, shift);
    temp = multPointMatrix(temp , pm);
    double projX = (temp(0,0) + 1) * 0.5 * imageWidth;
    double projY = (1 - ((temp(0,1) + 1) * 0.5)) * imageHeight;
    xco.push_back(projX);
    yco.push_back(projY);
    //cout << projX << ", "<< projY << std::endl;
  }

  ifstream myFile1 ("/Users/ankurM/Development/cv/labs/shapes/tetrahedronEdges.txt");
  getline (myFile1,line);
  istringstream iss1(line);
  size = 0; iss1 >> size;
  //cout << size <<  endl;
  if (myFile1.is_open())
  {
    while (getline (myFile1,line) )
    {
      int a, b;
      istringstream iss(line);
      iss >> a >> b;
      int x1 = xco.at(a); int y1 = yco.at(a);
      int x2 = xco.at(b); int y2 = yco.at(b);
      int steps = 2.5 * max(abs(x2-x1), abs(y2-y1)) ;
      for(double i = 0; i < steps; ++i) {
        xco.push_back(x1 + ((i)/(steps)*(x2-x1)));
        yco.push_back(y1 + ((i)/(steps)*(y2-y1)));
      }
    }
    myFile1.close();
  }

  set< pair<int, int> > kek;
  for (int i = 0; i < xco.size(); i++) {
	  pair<int, int> p;
	  p.first = xco.at(i);
	  p.second = yco.at(i);
      kek.insert(p);
  }

  cout << "P3 " <<imageWidth<< " " <<imageHeight<<" 1" << endl;
  for (int i = 0; i < imageWidth * 3; ++i) {
	  for (int j = 0; j < imageHeight ; ++j) {
		  pair<int, int> p;
		  p.first = i;
		  p.second = j;
		  if (kek.find(p) != kek.end()) cout << " 1 1 1 ";
		  else cout << " 0 0 0 ";
	  }
  }
  return 0;
}
