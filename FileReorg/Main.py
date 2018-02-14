import os
import sys

import Config as conf
import Functions as fn

import numpy as np
import cv2

#Open the video file
cap = cv2.VideoCapture('tc_29.97fps_df_20min.mov')

fps = 0
frames = 0
width = 0
height = 0

if cap.isOpened():
	fps = cap.get(cv2.CAP_PROP_FPS)
	frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
	width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
	height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
	msecs = cap.get(cv2.CAP_PROP_POS_MSEC)
	time_length = int(frames / fps)

frame_increment = int((frames * 0.9) / 24)
frame_counter = int(frames * 0.05)

success = True

while success:
	cap.set(1, frame_counter)
	success, frame = cap.read()
	if success:
		cv2.imwrite("frame_%d.jpg" % frame_counter, frame)
		frame_counter += frame_increment



cap.set(1, milliseconds_increments_counter)
success, frame = cap.read()
cv2.imwrite("frame_%d.jpg" % milliseconds_increments_counter, frame)
milliseconds_increments_counter = 35000

cap.set(1, milliseconds_increments_counter)
success, frame = cap.read()
cv2.imwrite("frame_%d.jpg" % milliseconds_increments_counter, frame)
milliseconds_increments_counter += 100

cap.set(1, milliseconds_increments_counter)
success, frame = cap.read()
cv2.imwrite("frame_%d.jpg" % milliseconds_increments_counter, frame)


while success:
	cap.set(1, milliseconds_increments_counter)
	success, frame = cap.read()
	cv2.imwrite("frame_%d.jpg" % milliseconds_increments_counter, frame)
	milliseconds_increments_counter += milliseconds_increments

#Store this frame to an image

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()



#	m, s = divmod(3577, 60)
#	h, m = divmod(m, 60)
#	if h > 0:
#		print "%02d:%02d:%02d" % (h, m, s)
#	else:
#		print "%02d:%02d" % (m, s)

#success,image = vidcap.read()
#count = 40
#success = True
#while success:
#	success,image = vidcap.read()
#	print('Read a new frame: ', success)
#	cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
#	count += 40

#if (len(sys.argv) > 1) and os.path.isdir(sys.argv[1]):
#	conf.paths = [sys.argv[1].strip()]
#	print "Folder: " + sys.argv[1]
#	resp = raw_input("Reorganize folder? (y/n): ")
#	print ""
#	conf.reorg = resp.strip().lower() == "y"

## delete unwanted files
#for dir in conf.paths:
	
#	fn.DeleteUnwatedFiles(dir)

#	if conf.reorg:
#		fn.RenameMove(dir)

