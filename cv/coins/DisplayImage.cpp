#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <Image_Path>\n");
        return -1;
    }

    Mat image, gray_image;
    image = imread( argv[1], 1 );
    cvtColor( image, gray_image, CV_BGR2GRAY );
    if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }

    imwrite( "Gray_Image.jpg", gray_image );

    namedWindow( "Display image", CV_WINDOW_AUTOSIZE );
    namedWindow( "Gray image", CV_WINDOW_AUTOSIZE );

    imshow( "Display image", image );
    imshow( "Gray image", gray_image );

    waitKey(0);

    return 0;
}
