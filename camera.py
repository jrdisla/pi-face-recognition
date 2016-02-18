import subprocess

import config

def take_pic(file):
	code = subprocess.call("fswebcam -r 640x480 --no-banner " + file, shell = True)
	return code