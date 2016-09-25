#include <iostream>
#include<fstream>
#include <sstream>
#include <matrix.cpp>
using namespace std;

int main() {
    string line;
    ifstream myFile ("coordinates.txt");
    int a,b,c;
    if (myFile.is_open())
    {
        while (getline (myFile,line) )
        {
            istringstream iss(line);
            iss >> a >> b >> c;
            cout << a << " " << b << " " << c << endl;

        }
        myFile.close();
    }

    else cout << "Unable to open file";

    return 0;
}
