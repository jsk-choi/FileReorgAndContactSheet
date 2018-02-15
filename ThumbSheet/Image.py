import numpy as np
import cv2

def TimecodeImage(seconds):

	m, s = divmod(seconds, 60)
	h, m = divmod(m, 60)

	timecode = "%02d:%02d:%02d" % (h, m, s)

	time_code_background_image = np.zeros((40, 186, 3), np.uint8)
	cv2.putText(time_code_background_image, timecode, (1, 33), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255,255,255), 2, cv2.LINE_AA)
	return time_code_background_image 
