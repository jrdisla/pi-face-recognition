#Samples for face detection and recognition on Rasperry Pi

Most of code is copied from [https://learn.adafruit.com/raspberry-pi-face-recognition-treasure-box/overview](https://learn.adafruit.com/raspberry-pi-face-recognition-treasure-box/overview).

##Setup

Install fswebcam package by running `sudo apt-get install fswebcam`

Run `sudo apt-get install python-opencv` to install Python OpenCV package.

##Other commands

Take picture with webcam `fswebcam -r 640x480 --no-banner filename.jpg`