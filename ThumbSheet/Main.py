import os
import sys
import cv2
import collections

import Classes as cl
import Image as img

#Open the video file
vid_attr = cl.vid_attr('ppil.mp4', 8, 6, 0.05)

frame_counter = vid_attr.startframe

thumbs_dict = {}
success = True

for ii in range(1, vid_attr.totalthumbs + 1):
	if not success:
		break

	vid_attr.vid_cap.set(1, frame_counter)
	success, frame = vid_attr.vid_cap.read()

	if success:
		print "frame grabbed %d" % frame_counter
		thumbs_dict[frame_counter] = img.overlay_timecode_on_thumbnail(int(frame_counter / vid_attr.fps), frame)
		frame_counter += vid_attr.frameinterval


for key in collections.OrderedDict(sorted(thumbs_dict.items())):
	filename = "frame_%d.jpg" % key
	print "write " + filename
	cv2.imwrite("frame_%d.jpg" % key, thumbs_dict[key])

