#!/usr/bin/python3
import cv2
#function to create difference image 
#x,y,z are three image frames
def create_image_diff(x,y,z):
	image1_diff=cv2.absdiff(x,y)
	image2_diff=cv2.absdiff(y,z)
	image3_diff=cv2.bitwise_and(image1_diff,image2_diff)
	return image3_diff
#starting web cam 
cap = cv2.VideoCapture(0)
frame1 = cap.read()[1]
frame2 = cap.read()[1]
frame3 = cap.read()[1]
#converting into gray scale 
gray1= cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2= cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
gray3= cv2.cvtColor(frame3,cv2.COLOR_BGR2GRAY)

while True:
	new_image = create_image_diff(gray1,gray2,gray3)
	cv2.imshow('window',new_image)
	#capture new image 
	status,frame4 = cap.read()
	cv2.imshow('original',frame4)
	#exchange pics
	gray1=gray2
	gray2=gray3
	gray3=cv2.cvtColor(frame4,cv2.COLOR_BGR2GRAY)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()