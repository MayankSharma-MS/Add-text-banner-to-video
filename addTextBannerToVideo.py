import numpy as np
import cv2
import moviepy.editor as mp
from moviepy.editor import *
import subprocess

# path to input video that needs to be edited
inputVideoPath = "input\\honor.mp4"

# path where you want your edited video to be saved
outputVideoPath = "output\\"

video = mp.VideoFileClip(inputVideoPath)

# type text here, line 1 and line 2 will appear above the video
# while line 3 aur line 4 appears below.
line1 = " Everyone out there who thinks gaming"
line2 = " is for kids..watch this"
line3 = "This is a master piece, perfect blend"
line4 = "of GOT and Vikings <3 <3 "


# eneter your watermark text or your company name, levave it blank like this "" if you do not want any watermarl on video
watermarkText = "https://github.com/MayankSharma-MS/Add-text-banner-to-video"

# enter your desired font size below, can be in decimal too 0.1 or 1.3 or 2
fontsize = 2


# background color of bannner, do not change this section
white_background=255
black_background=0


topBanner = None
bottomBanner = None

cap = cv2.VideoCapture(inputVideoPath)

# remove # from below line if you want to record live from camera 
#cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
print(cap.isOpened())
while(cap.isOpened()):
	ret, frame = cap.read()
	if frame is None: break
	height, width, ch = frame.shape
	cv2.putText(frame, watermarkText, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (225, 225, 255), 2)

	if out is None:
		out = cv2.VideoWriter(outputVideoPath+'output12.mp4',fourcc, video.fps, (width, height+ 2*(fontsize*100)), True)
		topBanner = np.ones([fontsize*100, width, 3], dtype=np.uint8)
		bottomBanner = np.ones([fontsize*100, width, 3], dtype=np.uint8)
		topBanner.fill(black_background)
		bottomBanner.fill(black_background)
		## put text in banner ##
		cv2.putText(topBanner, line1, (10, 50 + fontsize*20), cv2.FONT_HERSHEY_SIMPLEX,
					fontsize, (255, 110, 255), 5)
		cv2.putText(topBanner, line2, (10, fontsize*40+(50 + fontsize*20)), cv2.FONT_HERSHEY_SIMPLEX,
					fontsize, (255, 110, 255), 5)
		cv2.putText(bottomBanner, line3, (10, 50 + fontsize*20), cv2.FONT_HERSHEY_SIMPLEX,
					fontsize, (255, 110, 255), 5)
		cv2.putText(bottomBanner, line4, (10, fontsize*40+(50 + fontsize*20)), cv2.FONT_HERSHEY_SIMPLEX,
					fontsize, (255, 110, 255), 5)

	
	#cv2.imshow("resize", frame)
	#print(frame.shape, height, width)
	output = np.vstack((topBanner, frame, bottomBanner))

	out.write(output)
	#cv2.imshow('frame',output)
	if cv2.waitKey(1) & 255 == 27:
		break

cap.release()
out.release()
cv2.destroyAllWindows()

command = "echo y | ffmpeg -i "+ outputVideoPath +"output12.mp4 -i "+ inputVideoPath + " -codec copy -shortest " + outputVideoPath + "converted_video.mp4"
subprocess.call(command, shell=True)

command = "del "+ outputVideoPath + "output12.mp4"
subprocess.call(command, shell=True)

print ("\n conversion successfully completed. Find your output video at "+outputVideoPath+"converted_video.mp4")