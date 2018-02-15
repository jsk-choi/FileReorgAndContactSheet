import numpy as np
import cv2

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