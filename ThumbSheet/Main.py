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

filename = "ppil.mp4"

vid_attr = cl.vid_attr(filename, conf.thumbs_horizontal, conf.thumbs_vertical, conf.video_pad)

header_height, thumb_height, template_image = img.create_image_template(filename)
thumbs = cap.capture_thumbnails(filename)

conf.thumb_height = thumb_height

counter = 0
thumbs_keys = list(thumbs.keys())
thumbnail_scale = (thumb_height * 1.0) / thumbs[thumbs_keys[0]].shape[0]
x_offset = conf.thumb_spacing
y_offset = header_height

for y in range (1, conf.thumbs_vertical + 1):

	y_offset += conf.thumb_spacing + conf.thumb_height

	for x in range(1, conf.thumbs_horizontal):

		thumbnail = thumbs[thumbs_keys[counter]]
		thumbnail_scaled = cv2.resize(thumbnail, (0, 0), fx = thumbnail_scale, fy = thumbnail_scale, interpolation = cv2.INTER_AREA)
		template_image[y_offset: y_offset + thumbnail_scaled.shape[0], x_offset: x_offset + thumbnail_scaled.shape[1]] = thumbnail_scaled
		
		x_offset += (conf.thumb_spacing * 2) + conf.thumb_width
		counter += 1

	x_offset = conf.thumb_spacing

cv2.imwrite("zzzooo.png", template_image)

#for key in thumbs:

#	thumb_scale = (thumb_height * 1.0) / thumbs[key].shape[0]
#	scaled_thumb = cv2.resize(thumbs[key], (0, 0), fx = thumb_scale, fy = thumb_scale, interpolation = cv2.INTER_AREA)

#	cv2.imwrite("zzz templ.png", template_image)
#	cv2.imwrite("zzz thumb.png", scaled_thumb)
	
#	x_offset = conf.thumb_spacing
#	y_offset = header_height
#	template_image[y_offset: y_offset + scaled_thumb.shape[0], x_offset: x_offset + scaled_thumb.shape[1]] = scaled_thumb
#	cv2.imwrite(str(key) + ".png", template_image)
#	break

