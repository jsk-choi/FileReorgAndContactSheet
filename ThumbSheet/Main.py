import os
import sys
import cv2
import collections

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import Capture as cap
import Config as conf
import Classes as cl
import Image as img


space = 10
im_sm = cv2.imread("im_sm.png")
im_lg = cv2.imread("im_lg.png")
x_offset = y_offset = space
for y in range(1, 12):
	for x in range(1, 24):
		im_lg[y_offset: y_offset + im_sm.shape[0], x_offset: x_offset + im_sm.shape[1]] = im_sm
		x_offset += (im_sm.shape[1]  + space)
	x_offset = space
	y_offset += (im_sm.shape[0]  + space)

#for y in range(1, 3):
#	for x in range(1, 3):
#		#im_lg[y_offset: ((y_offset + im_sm.shape[0]) * y), x_offset: (x_offset + im_sm.shape[1]) * x] = im_sm

cv2.imwrite("zzzooo.png", im_lg)



filename = "ppil.mkv"

vid_attr = cl.vid_attr(filename, conf.thumbs_horizontal, conf.thumbs_vertical, conf.video_pad)

header_height, thumb_height, template_image = img.create_image_template(filename)
thumbs = cap.capture_thumbnails(filename)

conf.thumb_height = thumb_height

counter = 0
thumbs_keys = list(thumbs.keys())
thumbnail_scale = (conf.thumb_height * 1.0) / thumbs[thumbs_keys[0]].shape[0]
x_offset = conf.thumb_spacing
y_offset = header_height

for y in range (1, conf.thumbs_vertical + 1):

	for x in range(1, conf.thumbs_horizontal + 1):

		thumbnail = thumbs[thumbs_keys[counter]]
		thumbnail_scaled = cv2.resize(thumbnail, (conf.thumb_width, conf.thumb_height), interpolation = cv2.INTER_AREA)
		template_image[y_offset: y_offset + thumbnail_scaled.shape[0], x_offset: x_offset + thumbnail_scaled.shape[1]] = thumbnail_scaled		

		cv2.imwrite("thm_x{0}y{1}.png".format(x, y), template_image)

		x_offset += conf.thumb_spacing + conf.thumb_width
		counter += 1

	x_offset = conf.thumb_spacing
	y_offset += (conf.thumb_height + conf.thumb_spacing)

cv2.imwrite("zzzooo.png", template_image)

for key in thumbs:

	thumb_scale = (thumb_height * 1.0) / thumbs[key].shape[0]
	scaled_thumb = cv2.resize(thumbs[key], (0, 0), fx = thumb_scale, fy = thumb_scale, interpolation = cv2.INTER_AREA)

	cv2.imwrite("zzz templ.png", template_image)
	cv2.imwrite("zzz thumb.png", scaled_thumb)
	
	x_offset = conf.thumb_spacing
	y_offset = header_height
	template_image[y_offset: y_offset + scaled_thumb.shape[0], x_offset: x_offset + scaled_thumb.shape[1]] = scaled_thumb
	cv2.imwrite(str(key) + ".png", template_image)
	break

