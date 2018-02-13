#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

Mat src, src_gray, gauss, dst;

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: ./CountCoins <Image_Path>\n");
        return -1;
    }

    src = imread(argv[1], 1);
    cvtColor(src, src_gray, CV_BGR2GRAY);
    if ( !src.data )
    {
        printf("No image data \n");
        return -1;
    }
    GaussianBlur(src_gray, gauss, Size(7,7), 7 , 7);
    /*Canny( gauss, gauss, lowThreshold, lowThreshold*ratio, kernel_size );
    dst = Scalar::all(0);
    src.copyTo( dst, gauss);
    imshow( window_name, dst );*/
    
    vector<Vec3f> coin;
    HoughCircles(gauss, coin, CV_HOUGH_GRADIENT, 1, 100, 38, 100 , 30, 289);
    cout << src_gray.rows/8;
    for( size_t i = 0; i < coin.size(); i++ )
    {
	Point center(cvRound(coin[i][0]),cvRound(coin[i][1]));
	int radius=cvRound(coin[i][2]);
        circle(src,center,3,Scalar(0,255,0),-1,8,0);     
        circle(src,center,radius,Scalar(0,0,255),3,8,0);
	cout<< " Center location for circle "<<i+1<<" : "<<center<<"\n Diameter : "<<2*radius<<"\n";
     }
    cout<<"\n";
    imwrite( "coins_count.jpg", src);
  
    waitKey(0);

    return 0;
}
