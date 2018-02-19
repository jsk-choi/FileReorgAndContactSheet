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

		#cv2.imwrite("thm_x{0}y{1}.png".format(x, y), template_image)

		x_offset += conf.thumb_spacing + conf.thumb_width
		counter += 1

	x_offset = conf.thumb_spacing
	y_offset += (conf.thumb_height + conf.thumb_spacing)

cv2.imwrite("zzzooo.png", template_image)

