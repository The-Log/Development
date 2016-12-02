#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

int w, h;

vector<int> blurrer(vector<int> gray) {
	vector<int> blur;
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			if (i == 0 || i == w - 1 || j == 0 || j == h - 1) blur.push_back(gray[i * w + j]);
			else blur.push_back((4*gray[i*w+j] + 2*gray[(i-1)*w+j] + 2*gray[(i+1)*w+j] + 2*gray[i*w+j-1] + 2*gray[i*w+j+1] + gray[(i+1)*w+j+1] + gray[(i-1)*w+j+1] + gray[(i+1)*w+j-1] + gray[(i-1)*w+j-1])/16);
		}
	}
	return blur;
}

set<int> sobel(vector<int> l) {
	set<int> s;
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			if (i > 2 || i < h - 2 || j > 2 || j < w - 2) {
				int n = h;
				int lx = -l[(i-1)*n+j+1] + l[(i+1)*n+j+1] - 2*l[(i-1)*n+j] + 2*l[(i+1)*n+j] - l[(i-1)*n+j-1] + l[(i+1)*n+j-1];
                int ly = -l[(i-1)*n+j+1] - l[(i+1)*n+j+1] - 2*l[i*n+j+1] + 2*l[i*n+j-1] + l[(i-1)*n+j-1] + l[(i+1)*n+j-1];
				if (abs(lx) + abs(ly) > 90) s.insert(i * w + j);
			}
		}
	}
	return s;
}

int main() {
	string line;
	ifstream f("image3.ppm");
	getline(f,line);
	getline(f,line);
	istringstream iss(line);

	iss >> w >> h;
	getline(f,line);
	vector<int> gray;
	set<int> dilate;
	vector<int> dank;
	while (getline(f,line)) {
		istringstream iss(line);
		vector<int> num;
		string tmp;
		while (getline(iss, tmp, ' ')) {
			num.push_back(stoi(tmp));
		}

		for (int i = 0; i < num.size() - 2; i+=3) {
			gray.push_back(0.30 * num[i] + 0.59 * num[i+1] + 0.11 * num[i+2]);
			int tt = round((num[i] + num[i+1] + num[i+2])/(3*255.0));
			//gray.push_back(tt);
			dank.push_back(1);
		}
	}

	for (int i = 0; i < gray.size(); ++i) {if (gray[i] == 0) dilate.insert(i);}

	int dx[8] = {1,1,1,-1,-1,-1,0,0};
	int dy[8] = {0,h,-h,0,h,-h,h,-h};

	for (auto f:dilate) {
		//cout << f << endl;
		for (int i = 0; i < 8; ++i) {
			//if ((f/w+dx[i])*w+f%w+dy[i] > -1 && (f/w+dx[i])*w+f%w+dy[i] < w * h) {
			//	dank[(f/w+dx[i])*w+f%w+dy[i]] = 1;
			//}
			if (f/w+dx[i] > -1 && f/w+dx[i] < w && f%w+dy[i] > -1 && f%w+dy[i] < h){
				//cout << (f/w+dx[i])*w+f%w+dy[i] << endl;
				dank[(f/w+dx[i])*w+f%w+dy[i]] = 0;
			}
		}
	}


	/*vector<int> blur;
	for (int i = 0; i < h; ++i) {
		for (int j = 0; j < w; ++j) {
			if (i == 0 || i == w - 1 || j == 0 || j == h - 1) blur.push_back(gray[i * w + j]);
			else blur.push_back((4*gray[i*w+j] + 2*gray[(i-1)*w+j] + 2*gray[(i+1)*w+j] + 2*gray[i*w+j-1] + 2*gray[i*w+j+1] + gray[(i+1)*w+j+1] + gray[(i-1)*w+j+1] + gray[(i+1)*w+j-1] + gray[(i-1)*w+j-1])/16);
		}
	}*/

	for (int i = 0; i < 9; ++i) gray = blurrer(gray);
	set<int> s = sobel(gray);

	cout << "P3 " << w << " " << h << " 1" << endl;
	/*for (int i = 0; i < gray.size(); ++i) {
		if (dank[i] == 0 && gray[i] != 0) {
			cout << " 0 0 0";
		} else {
			cout << " 1 1 1";

		}
		//cout << gray[i] << " " << gray[i] << " " << gray[i] << " ";
	}*/

	for (int i = 0; i < gray.size(); ++i) {
		if (s.find(i) == s.end()) cout << " 1 1 1";
		else cout << " 0 0 0";
	}

	return 0;
}
