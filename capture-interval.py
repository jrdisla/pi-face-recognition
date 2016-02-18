import cv2
import time

import config
import camera

pic_nr = 0;

while True:
	img_name = config.CAPTURE_DIR + str(pic_nr) + ".jpg"
	camera.take_pic(img_name)
	pic_nr = pic_nr + 1
	time.sleep(60)