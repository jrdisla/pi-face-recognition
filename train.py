import fnmatch
import os

import cv2
import numpy as np

import config
import face

def walk_files(directory, match = "*"):
	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)

def prep_image(filename):
	return face.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

def normalize(X, low, high, dtype = None):
	X = np.asarray(X)
	minX, maxX = np.min(X), np.max(X)
	# normalize to [0...1].
	X = X - float(minX)
	X = X / float((maxX - minX))
	# scale to [low...high].
	X = X * (high - low)
	X = X + low
	if dtype is None:
		return np.asarray(X)
	return np.asarray(X, dtype = dtype)

print "Reading training images ..."
faces = []
labels = []
pos_count = 0
neg_count = 0
	
# Read all positive images
for filename in walk_files(config.POSITIVE_DIR, "*.jpg"):
	faces.append(prep_image(filename))
	labels.append(1)
	pos_count += 1

# Read all negative images
for filename in walk_files(config.NEGATIVE_DIR, "*.pgm"):
	faces.append(prep_image(filename))
	labels.append(0)
	neg_count += 1

print "Read", pos_count, "positive images and", neg_count, "negative images."

# Train model
print "Training model ..."
model = cv2.createEigenFaceRecognizer()
model.train(np.asarray(faces), np.asarray(labels))

# Save model results
model.save(config.TRAINING_FILE)
print "Training data saved to ...", config.TRAINING_FILE

mean = model.getMat("mean").reshape(faces[0].shape)
cv2.imwrite(config.MEAN_FILE, normalize(mean, 0, 255, dtype = np.uint8))
eigenvectors = model.getMat("eigenvectors")
pos_eigenvector = eigenvectors[:,0].reshape(faces[0].shape)
cv2.imwrite(config.POSITIVE_EIGENFACE_FILE, normalize(pos_eigenvector, 0, 255, dtype = np.uint8))
neg_eigenvector = eigenvectors[:,1].reshape(faces[0].shape)
cv2.imwrite(config.NEGATIVE_EIGENFACE_FILE, normalize(neg_eigenvector, 0, 255, dtype = np.uint8))