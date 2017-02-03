#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;

int main(int argc, char** argv){

  string source = argv[1];
  std::cout  << "Source File: " << source << std::endl;
  VideoCapture input(source);
  if (!input.isOpened()){
    std::cout  << "Could not open the input video: " << source << std::endl;
    return -1;
  }
  std::cout  << "read!" << std::endl;

  Size S = Size((int) input.get(CV_CAP_PROP_FRAME_WIDTH), (int) input.get(CV_CAP_PROP_FRAME_HEIGHT));
  VideoWriter output("output.avi", input.get(CV_CAP_PROP_FOURCC), input.get(CV_CAP_PROP_FPS), S, true);
  if (!output.isOpened()){
        std::cout << "Output video could not be opened" << std::endl;
        return -1;
  }
  
  Mat src, out;

  while(true){
    input >> src;
    if (!src.data){
        printf("Finished Reading \n");
        break;
    }

    /*
      Project cube into source image and adjust for rotatations/zooming it as the video progresses
    */

    output.write(out);
    int c = cvWaitKey(10);
    if(c == 27) break;
  }
  output.release();
  return 0;
}
