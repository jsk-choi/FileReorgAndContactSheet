import os
import sys
import cv2
import collections

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import Config as conf
import Classes as cl
import Image as img


vid_attr = cl.vid_attr('ppil.mp4', conf.thumbs_horizontal, conf.thumbs_vertical, conf.video_pad)


#                       w     h
im = Image.new('RGBA', (200, 1000), conf.background_color)

draw = ImageDraw.Draw(im)
draw.text((20, 150), 'Hello', fill='red')
courier_font = ImageFont.truetype(os.path.join(r'courbd.ttf'), 13)
draw.text((100, 150), 'Face', fill='black', font=courier_font)

img_ = np.array(im)

cv2.imwrite("img_.png", img_)




## open the video file
#vid_attr = cl.vid_attr('big_buck_bunny.mp4', conf.thumbs_horizontal, conf.thumbs_vertical, conf.video_pad)

#frame_counter = vid_attr.startframe

#thumbs_dict = {}
#success = True

#for ii in range(1, vid_attr.totalthumbs + 1):
#	if not success:
#		break

#	vid_attr.vid_cap.set(1, frame_counter)
#	success, frame = vid_attr.vid_cap.read()

#	if success:
#		print "frame grabbed %d" % frame_counter
#		thumbs_dict[frame_counter] = img.overlay_timecode_on_thumbnail(int(frame_counter / vid_attr.fps), frame)
#		frame_counter += vid_attr.frameinterval


#for key in collections.OrderedDict(sorted(thumbs_dict.items())):
#	filename = "frame_%d.jpg" % key
#	print "write " + filename
#	cv2.imwrite("frame_%d.jpg" % key, thumbs_dict[key])

