#include <stdio.h>
#include "opencv2/imgproc/imgproc.hpp"
#include <opencv2/opencv.hpp>

using namespace cv;

Mat src, gray_src, out, detected_edges;

int const my_threshold = 12;
string window_name = "edgyCamera";

int main(int argc, char** argv )
{
    VideoCapture cap(0);

    /*VideoWriter outputVideo;
    Size S = Size((int) cap.get(CV_CAP_PROP_FRAME_WIDTH), (int) cap.get(CV_CAP_PROP_FRAME_HEIGHT));
    outputVideo.open("output.avi", cap.get(CV_CAP_PROP_FOURCC), cap.get(CV_CAP_PROP_FPS), S, true);*/

    while(true){
      cap >> src;
      if ( !src.data ){
          printf("Derp! \n");
          return -1;
      }
      cvtColor( src, gray_src, CV_BGR2GRAY );
      namedWindow(window_name, WINDOW_AUTOSIZE );
      blur( gray_src, detected_edges, Size(3,3) );
      Canny( detected_edges, detected_edges, my_threshold, my_threshold*3, 3 );
      out = Scalar::all(0);
      src.copyTo(out, detected_edges);
      cvtColor(out, out, CV_BGR2GRAY);
      imshow(window_name, out);
      int c = cvWaitKey(10);

      //outputVideo.write(out);

      if(c == 27) break;
    }
    return 0;
}
