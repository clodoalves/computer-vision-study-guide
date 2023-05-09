#include "OpenCVBasicSamples.h"
#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>

using namespace cv;
using namespace std;

void LoadImage()
{
	Mat image = imread("Content/Images/people1.jpg");

	if (image.empty())
	{
		cout << "Could not open or find the image" << endl;
		system("pause"); 
	}

	String windowName = "My HelloWorld Window"; 

	namedWindow(windowName); 

	imshow(windowName, image); 

	waitKey(0); 


	destroyWindow(windowName);
}

void PlayVideo() 
{
	VideoCapture cap("Content/Videos/street.mp4");

	if (!cap.isOpened()) 
	{
		cout << "Cannot open the video file" << endl;
		cin.get();
	}

	double fps = cap.get(CAP_PROP_FPS);
	cout << "Frames per seconds: " << fps << endl;

	string windowName = "My First Video";

	namedWindow(windowName, WINDOW_NORMAL);

	bool success = true;

	while (success) 
	{
		Mat frame;

		bool success = cap.read(frame);

		if (success)
			imshow(windowName, frame);

		if (waitKey(10) == 27)
		{
			cout << "Esc key is pressed by user. Stoppig the video" << endl;
			break;
		}
	}

	cout << "End of the video" << endl;
}

void PlayVideoFromWebCam() 
{
}