import fnmatch
import os

import cv2

import config
import face

model = cv2.createEigenFaceRecognizer()
model.load(config.TRAINING_FILE)

def walk_files(directory, match = "*"):
	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)

for filename in walk_files(config.TEST_DIR, "*.jpg"):
	
	img = cv2.imread(filename)
	bw_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	result = face.detect_single(bw_img)

	if result is None:
		print filename, "No face detected ..."
	else:
		x, y, w, h = result
		crop = face.resize(face.crop(bw_img, x, y, w, h))
		label, confidence = model.predict(crop)
		print filename, "label ... '%s'" % label, "confidence ... '%s'" % confidence