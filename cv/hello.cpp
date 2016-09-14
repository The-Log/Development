#include <iostream>, <cmath>

using namespace std;

int main(void)
{
  int x = 2;
  if(x != 3)
    std:: cout << "x = " << --x;
  else
    std :: cout << "x == 3";
  int larger;
  int x = 5;
  int y = 9;
  if (x > y){
      larger = x;
  }
  else
      larger = y;
  return 0;
}
