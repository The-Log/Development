#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

using namespace cv;
using namespace std;

std::vector<cv::Point3f> Create3DChessboardCorners(cv::Size boardSize, float squareSize)
{
  // This function creates the 3D points of your chessboard in its own coordinate system
 
  std::vector<cv::Point3f> corners;
 
  for( int i = 0; i < boardSize.height; i++ )
  {
    for( int j = 0; j < boardSize.width; j++ )
    {
      corners.push_back(cv::Point3f(float(j*squareSize),
                                float(i*squareSize), 0));
    }
  }
 
  return corners;
}
Mat draw(Mat img, vector<Point2f> projectedPoints ){
  line(img, projectedPoints.at(0), projectedPoints.at(1), Scalar(0,255,0), 3);
  line(img, projectedPoints.at(1), projectedPoints.at(2), Scalar(0,255,0), 3);
  line(img, projectedPoints.at(2), projectedPoints.at(3), Scalar(0,255,0), 3);
  line(img, projectedPoints.at(0), projectedPoints.at(3), Scalar(0,255,0), 3);

  line(img, projectedPoints.at(0), projectedPoints.at(4), Scalar(0,0,255), 3);
  line(img, projectedPoints.at(1), projectedPoints.at(5), Scalar(0,0,255), 3);
  line(img, projectedPoints.at(2), projectedPoints.at(6), Scalar(0,0,255), 3);
  line(img, projectedPoints.at(3), projectedPoints.at(7), Scalar(0,0,255), 3);

  line(img, projectedPoints.at(4), projectedPoints.at(5), Scalar(255,0,0), 3);
  line(img, projectedPoints.at(5), projectedPoints.at(6), Scalar(255,0,0), 3);
  line(img, projectedPoints.at(6), projectedPoints.at(7), Scalar(255,0,0), 3);
  line(img, projectedPoints.at(7), projectedPoints.at(4), Scalar(255,0,0), 3);

  return img;
}

int main(int argc, char** argv){

  if ( argc != 2 ) {
    printf("usage: ./CountCoins <Video_Path>\n");
    return -1;
  }
  
  String source = argv[1];
  std::cout  << "Source File: " << source << std::endl;
  VideoCapture sauce(source);
  VideoWriter outputVideo;
  if (!sauce.isOpened()){
    std::cout  << "Could not open the input video: " << source << std::endl;
    return -1;
  }  
  while(1){
    Mat frame;
    Mat imgGray;

    sauce >> frame;

    if (frame.empty())
      break;

    flip(frame, frame, 0);

    cvtColor( frame, imgGray, CV_BGR2GRAY );
    
    Size board_sz = Size(7, 7);
    vector<Point2f> corners;
    
    bool found = findChessboardCorners(imgGray, board_sz, corners, CV_CALIB_CB_ADAPTIVE_THRESH + CV_CALIB_CB_NORMALIZE_IMAGE + CV_CALIB_CB_FAST_CHECK );
    if(found){
      cornerSubPix(imgGray, corners, Size(11, 11), Size(-1, -1),
                   TermCriteria(CV_TERMCRIT_EPS + CV_TERMCRIT_ITER, 30, 0.1));
      
      cv::Mat i_points = cv::Mat(corners);

      //drawChessboardCorners(frame, board_sz, corners, found);
      Mat cameraMatrix =  (Mat_<double>(3,3) <<  1.2195112968898779e+003, 0., 3.6448211117862780e+002, 0., 1.2414409169216196e+003, 2.4321803868732076e+002, 0., 0., 1.);
      
      vector<Point3f> op;

      vector<Point3f> axis;
      axis.push_back(cv::Point3f(0.0, 0, 0)); axis.push_back(cv::Point3f(0.0,4.0,0.0)); axis.push_back(cv::Point3f(4,4,0)); axis.push_back(cv::Point3d(4,0,0));
      axis.push_back(cv::Point3f(0,0,-4)); axis.push_back(cv::Point3f(0,4,-4)); axis.push_back(cv::Point3f(4,4,-4));axis.push_back(cv::Point3f(4,0,-4));

      op = Create3DChessboardCorners(board_sz, 4.5);
      cv::Mat o_points = cv::Mat(op);

      Mat distCoeffs = Mat::zeros(4,1,DataType<double>::type);
      distCoeffs.at<double>(0) = 0;
      distCoeffs.at<double>(1) = 0;
      distCoeffs.at<double>(2) = 0;
      distCoeffs.at<double>(3) = 0;
      
      Mat r_vec; Mat t_vec;
      cv::solvePnP(o_points, i_points, cameraMatrix, distCoeffs, r_vec, t_vec);

      std::vector<cv::Point2f> projectedPoints;
      projectPoints(axis, r_vec, t_vec, cameraMatrix, distCoeffs, projectedPoints);
      
      cout << projectedPoints << endl;
      Mat img = draw(frame, projectedPoints);
      imshow( "Img", img );
    }
    else{
      cout << "board not found" << endl;
    }
    
    char c=(char)waitKey(25);
    if(c==27)
      break;
  }
  
  std::cout  << "read!" << std::endl;
  
  return 0;
}
