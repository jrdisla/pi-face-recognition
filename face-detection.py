import cv2

import config

faceCascade = cv2.CascadeClassifier(config.HAAR_FACES)

img = cv2.imread(config.TEST_FILE, 1)
bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(bw_img, 1.1, 5)

print "Found " + str(len(faces)) + " face(s) ..."

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imwrite(config.TEST_FILE, image)