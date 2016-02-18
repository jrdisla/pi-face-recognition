import fnmatch
import os

import cv2

import config
import face

def walk_files(directory, match = "*"):
	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)

for filename in walk_files(config.CAPTURE_DIR, "*.jpg"):
	
	img = cv2.imread(filename)
	bw_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	result = face.detect_single(bw_img)

	if result is None:
		print "No face detected ... " + filename
	else:
		x, y, w, h = result
		crop = face.resize(face.crop(img, x, y, w, h))
		cv2.imwrite(filename, crop)
		print "Cropped file ... ", filename