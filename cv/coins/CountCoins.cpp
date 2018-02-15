#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

Mat src, src_gray, gauss, dst;
int brown[] = {126, 105, 83};
int silver[] = {121, 116, 106};
float distanceF(int x1, int y1, int z1, int x2, int y2, int z2){
  return sqrt(pow(x1-x2,2.0)+pow(y1-y2,2.0)+pow(z1-z2,2.0));
}
int main(int argc, char** argv )
{
    if ( argc != 2 ) {
        printf("usage: ./CountCoins <Image_Path>\n");
        return -1;
    }
    
    src = src_gray = imread(argv[1], 1);
    if ( !src.data ){
        printf("No image data \n");
        return -1;
    }
    cvtColor(src, src_gray, COLOR_BGR2GRAY);

    /*
    for(int i = 0; i < src_gray.rows; i++){
        for(int j = 0; j < src_gray.cols; j++){
          double avg = src_gray.at<cv::Vec3b>(i,j)[0] + src_gray.at<cv::Vec3b>(i,j)[1] + src_gray.at<cv::Vec3b>(i,j)[2];
          avg = avg / 3;
          src_gray.at<cv::Vec3b>(i,j)[2] = avg;
          src_gray.at<cv::Vec3b>(i,j)[1] = avg;
          src_gray.at<cv::Vec3b>(i,j)[0] = avg;
          
        }
     }
    */
   
    GaussianBlur(src_gray, gauss, Size(7,7), 7 , 7);
    
    /*
    Canny( gauss, gauss, lowThreshold, lowThreshold*ratio, kernel_size );
    dst = Scalar::all(0);
    src.copyTo( dst, gauss);
    imshow( window_name, dst );
    */
    float amount = 0.00;
    int errors = 0;
    vector<Vec3f> coins;
    HoughCircles(gauss, coins, CV_HOUGH_GRADIENT, 1, 150, 38, 100 , 20, 289);
    float minRadius = coins[0][2];
    for(size_t i = 0; i < coins.size(); i++){
      if(minRadius > coins[i][2]){
        minRadius = float(coins[i][2]);
      }
    }
    cout << minRadius << endl;
    for( size_t i = 0; i < coins.size(); i++ ){
      Vec3f circ = coins[i];
      Point center(cvRound(coins[i][0]),cvRound(coins[i][1]));
      float radius= (coins[i][2]);
      if (minRadius * 3 > float(radius)){
        Mat roi = src(cv::Range(circ[1]-circ[2], circ[1]+ circ[2]+1), cv::Range(circ[0]-circ[2], circ[0]+circ[2]+1));
        cv::Mat1b mask(roi.rows, roi.cols);
        cv::Scalar mean = cv::mean(roi, mask);
        int redVal = int(mean[2]);
        int greenVal = int(mean[1]);
        int blueVal = int(mean[0]);
        
        
        
        float distanceBrown = distanceF(redVal, greenVal, blueVal, brown[0], brown[1], brown[2]);
        float distanceSilver = distanceF(redVal, greenVal, blueVal, silver[0], silver[1], silver[2]);
        float ratioRadius =  float(radius/minRadius);

        String s = "Coin ";
        stringstream convert;
        convert << i;
        s = s + convert.str();
        cout << " " << s <<"\'s Ratio Radius: " << ratioRadius << endl;
        cout<< " Center location for circle "<<i<<" : "<<center<<"\n Radius : "<<radius<<"\n\n";
        //cout <<" Coin " << i << " : rgb("<< redVal <<", "<< greenVal << ", "<< blueVal << ")"<< endl;
        if (ratioRadius > 2.1 && distanceSilver < distanceBrown){
          amount = amount + 1.00;
        }
        else if(ratioRadius > 1.3 && ratioRadius < 1.5 && distanceSilver < distanceBrown){
          amount = amount + .05;

        }
        else if(ratioRadius >= 1.0 && ratioRadius < 1.4 && distanceSilver > distanceBrown){
          amount = amount + .01;
        }
        else if(ratioRadius >= 1.0 && ratioRadius < 1.3 && distanceSilver < distanceBrown){
          amount = amount + .10;
        }
        else{
          amount = amount + .1;
          errors = errors + 1;
          cout <<"Coin " << i << "ERROR" << endl;
          //cout << distanceSilver << ", " << distanceBrown << endl;
          //cout << " Ratio Radius: " << ratioRadius << endl;
          
        }
        //imshow(s, roi);
        circle(src,center,3,Scalar(0,255,0),-1,8,0);     
        circle(src,center,radius,Scalar(0,0,255),3,8,0);
      
        
      }
    }
    
    cout<<"\n";
    cout << "Approximate Total Amount: $" << amount << endl;
    cout << errors << endl;
    imwrite( "coins_count.jpg", src);
    resize(src, src, Size(src.cols/2, src.rows/2));
    namedWindow( "coins count" ,CV_WINDOW_AUTOSIZE);
    imshow("coins count", src );
    waitKey(0);

    return 0;
}
