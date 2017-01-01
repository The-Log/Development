#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace std;
using namespace cv;

int main(int argc, char** argv){

  string source = argv[1];
  cout  << "Source File: " << source << endl;
  VideoCapture in(source);
  if (!in.isOpened()){
    cout  << "Could not open the input video: " << source << endl;
    return -1;
  }

  cout  << "read!" << endl;
  Size S = Size((int) in.get(CV_CAP_PROP_FRAME_WIDTH), (int) in.get(CV_CAP_PROP_FRAME_HEIGHT));
  VideoWriter out;
  out.open("output.avi", in.get(CV_CAP_PROP_FOURCC), in.get(CV_CAP_PROP_FPS), S, true);
  Mat src;

  for(;;){
    in.read(src);
    //cout << in.get(CV_CAP_PROP_POS_MSEC) << endl;
    std::cout << "Never Happens" << '\n';
  }
}
