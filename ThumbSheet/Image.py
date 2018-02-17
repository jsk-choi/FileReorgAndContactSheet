import os
import sys
import cv2
import collections

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import Config as conf
import Classes as cl

def create_image_template(filename):

	vid_attr = cl.vid_attr(filename, conf.thumbs_horizontal, conf.thumbs_vertical, conf.video_pad)

	thumb_height = int((vid_attr.height / (vid_attr.width * 1.0)) * conf.thumb_width)
	im_header = im_height = 0

	im_header += conf.thumb_spacing						# pad
	im_header += int(conf.text_font_size * 1.5)			# first line
	im_header += int(conf.text_font_size)				# second line
	im_header += int(conf.thumb_spacing / 2)			# pad
	im_height += ((thumb_height + conf.thumb_spacing) * conf.thumbs_vertical) + conf.thumb_spacing	# all the thumbs

	im = Image.new('RGBA', (conf.width, im_header + im_height), conf.background_color)
	draw = ImageDraw.Draw(im)
	courier_font = ImageFont.truetype(os.path.join(conf.text_font), conf.text_font_size)

	draw_text = vid_attr.filename
	pos_x = pos_y = conf.thumb_spacing
	draw.text((pos_x, pos_y), draw_text, fill='black', font=courier_font)

	draw_text = "{0}, {1}x{2}, {3}fps, {4}".format(\
		vid_attr.size_string, \
		vid_attr.width, \
		vid_attr.height, \
		vid_attr.fps_string, \
		vid_attr.length_string)

	pos_y += int(conf.text_font_size * 1.5)
	draw.text((pos_x, pos_y), draw_text, fill='black', font=courier_font)

	return im_header, thumb_height, cv2.cvtColor(np.array(im), cv2.COLOR_BGRA2BGR)

def overlay_timecode_on_thumbnail(time_in_seconds, thumbnail):
	
	# get timecode image
	tc_img = timecode_image(time_in_seconds)

	# calculate timecode image size ratio to thumbnail
	resize_ratio = (thumbnail.shape[1] * 0.35) / tc_img.shape[1]

	# resize timecode image
	tc_img_sized = cv2.resize(tc_img, (0,0), fx=resize_ratio, fy=resize_ratio) 

	# flip both thumbnail and timecode image on x,y axis
	# no need to calculate timecode image offset to place on bottom right corner
	l_img = cv2.flip(thumbnail, -1)
	s_img = cv2.flip(tc_img_sized, -1)

	# overlay timecode image on thumbnail
	x_offset = y_offset = 0
	l_img[y_offset: s_img.shape[0], x_offset: s_img.shape[1]] = s_img

	print 'overlay done %d' % time_in_seconds

	# flip thumbnail again
	return cv2.flip(l_img, -1)


def timecode_image(seconds):

	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)

	timecode = "%02d:%02d:%02d" % (h, m, s)

	time_code_background_image = np.zeros((107, 500, 3), np.uint8)
	cv2.putText(time_code_background_image, timecode, (3, 90), cv2.FONT_HERSHEY_DUPLEX, 3.45, (255,255,255), 6, cv2.LINE_AA)
	return time_code_background_image 