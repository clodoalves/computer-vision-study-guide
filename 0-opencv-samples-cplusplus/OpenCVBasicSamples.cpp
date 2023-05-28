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
	//Open default video camera
	VideoCapture cap(0);

	if (!cap.isOpened()) 
	{
		cout << "Cannot open the video camera" << endl;
		cin.get();
	}

	double framesWidth = cap.get(CAP_PROP_FRAME_WIDTH);
	double framesHeight = cap.get(CAP_PROP_FRAME_HEIGHT);


	cout << "Video resolution: " << framesWidth << "x" << framesHeight << endl;

	string windowName = "My camera";
	namedWindow(windowName);

	bool success = true;

	while (success) 
	{
		Mat frame; 
		success = cap.read(frame);

		if (success)
			imshow(windowName, frame);
		
		if (waitKey(10) == 27)
		{
			cout << "Esc key is pressed by user. Stoppig the video" << endl;
			break;
		}
	}
}

void SaveImageToFile()
{
	Mat image = imread("Content/Images/people1.jpg");

	if (image.empty())
	{
		cout << "Image not loaded" << endl;
		cin.get();

		return;
	}

	bool isImageLoaded = imwrite("D:/Folder/MyImage.jpg", image);

	if (!isImageLoaded) 
	{
		cout << "Failed to save" << endl;
		cin.get();

		return;
	}

	cout << "Image is succesfully saved to a file" << endl;

	string windowName = "Saved image";
	namedWindow(windowName);
	imshow(windowName, image);

	waitKey(0);


	destroyWindow(windowName);
}

void SaveWebcamFrameToFile() 
{
	VideoCapture cap(0);

	if (!cap.isOpened()) 
	{
		cout << "Cannot open the webcam" << endl;
		cin.get();
		return;
	}

	int frameWidth = static_cast<int>(cap.get(CAP_PROP_FRAME_WIDTH));
	int frameHeight = static_cast<int>(cap.get(CAP_PROP_FRAME_HEIGHT));

	Size frameSize(frameWidth, frameHeight);
	int framePerSecond = 10;

	VideoWriter videoWriter("D:/Folder/MyVideo.avi", VideoWriter::fourcc('M', 'J', 'P', 'G'), framePerSecond, frameSize, true);

	if(!videoWriter.isOpened()) 
	{
		cout << "Cannot save the video to a file";
		cin.get();
		return;
	}

	string windowName = "My camera feed";
	namedWindow(windowName);

	bool success = true;

	while (success) 
	{
		Mat frame;
		success = cap.read(frame);

		if (!success)
		{
			cout << "Video camera is disconnected" << endl;
			cin.get(); //Wait for any key press
			break;
		}

		videoWriter.write(frame);

		imshow(windowName, frame);

		if (waitKey(10) == 27) 
		{
			cout << "Esc key is pressed by user. Stoppig the video" << endl;
			break;
		}
	}

	videoWriter.release();
}