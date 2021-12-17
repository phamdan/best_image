from imutils import paths
import argparse
import cv2
import matplotlib.pyplot as plt
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()


list_test= "frame/IMG_5335/3"
save_image=None
fm_save=0
name=None
fms=[]
# loop over the input images

for imagePath in paths.list_images(list_test):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	fm = variance_of_laplacian(gray)
	fms.append(fm)
	if(fm >fm_save):
		fm_save = fm
		save_image =  image
		save_image = cv2.cvtColor(save_image, cv2.COLOR_BGR2RGB)
		name= imagePath

print("fms max",fm_save)
