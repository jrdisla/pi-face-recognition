import cv2
import time

import config
import face
import camera

model = cv2.createEigenFaceRecognizer()
model.load(config.TRAINING_FILE)

print "Model loaded ..."

while True:
	filename = config.TEST_FILE

	camera.take_pic(filename)

	img = cv2.imread(filename)
	bw_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	result = face.detect_single(bw_img)

	if result is None:
		print "No face detected ... :("
	else:
		x, y, w, h = result
		crop = face.resize(face.crop(bw_img, x, y, w, h))
		label, confidence = model.predict(crop)
		print "label ... '%s'" % label, "confidence ... '%s'" % confidence

	time.sleep(5)