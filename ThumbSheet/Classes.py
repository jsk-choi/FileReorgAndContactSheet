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
		self.totalthumbs = horiz_ct * vert_ct
		self.frameinterval = int((self.frames * (1 - (padding * 2))) / self.totalthumbs)
		self.startframe = int(self.frames * padding)

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
