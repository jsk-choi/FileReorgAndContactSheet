import os

import numpy as np
import cv2

class vid_attr:

	def __init__(self, vid_name, horiz_ct, vert_ct, padding):

		self.vid_cap = cv2.VideoCapture(vid_name)
		self.width = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
		self.height = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
		self.fps = int(self.vid_cap.get(cv2.CAP_PROP_FPS))
		self.frames = int(self.vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
		self.length = int(self.frames / self.fps)
		self.length_string = ""
		self.totalthumbs = horiz_ct * vert_ct
		self.frameinterval = int((self.frames * (1 - (padding * 2))) / self.totalthumbs)
		self.startframe = int(self.frames * padding)
		self.filename = vid_name.split(os.sep)[-1]
		self.size = os.path.getsize(vid_name)
		self.size_string = ""

		# self.length_string
		m, s = divmod(self.length, 60)
		h, m = divmod(m, 60)

		if h > 0:
			self.length_string = "%02d:%02d:%02d" % (h, m, s)
		else:
			self.length_string = "%02d:%02d" % (m, s)

		# self.size_string
		# gt MB
		if self.size > 1073741824:
			self.size_string = "%.1fGB" % (self.size / 1073741824.0)
		# gt MB
		elif self.size > 1048576:
			self.size_string = "%dMB" % int(self.size / 1048576.0)
		else:
			self.size_string = "%dKB" % int(self.size / 1024.0)


#class img_attr:

#	def __init__(self, vid_name):

#		vidCap = cv2.VideoCapture(vid_name)
#		self.width = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#		self.height = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#		self.fps = int(vid_cap.get(cv2.CAP_PROP_FPS))
#		self.frames = int(vid_cap.get(cv2.CAP_PROP_FRAME_COUNT))
#		self.length = int(self.frames / self.fps)
#		self.totalthumbs = horiz_ct * vert_ct
#		self.frameinterval = int((self.frames * (1 - (padding * 2))) / self.totalthumbs)
#		self.startframe = int(self.frames * padding)
