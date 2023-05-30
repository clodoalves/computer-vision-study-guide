#pragma once

void LoadImage();

void PlayVideo();

void PlayVideoFromWebCam();

void SaveImageToFile();

void SaveWebcamFrameToFile();

void ChangeImageBrightness(char* imagePath, int brightnessValue);

void ChangeImageContrast(char* imagePath, int contrastValue);

void GrayscaleImageHistogramEqualization(char* imagePath);

void ColorfulImageHistogramEqualization(char* imagePath);
