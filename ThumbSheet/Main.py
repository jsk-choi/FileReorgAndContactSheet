import os
import sys
import cv2

import Classes as cl
import Image

print "one"

thumb_dict = {}
thumb_dict[1] = "one"
thumb_dict[2] = "two"

durr = list(thumb_dict.keys())
 

#tc_img = Image.TimecodeImage(2974)

#cv2.imwrite("tc_img.png", tc_img)

#vid_attr = cl.vid_attr("big_buck_bunny.mp4", 8, 6, 0.05)

#resize_ratio = (vid_attr.width * 0.35) / tc_img.shape[1]

#tc_img_sized = cv2.resize(tc_img, (0,0), fx=resize_ratio, fy=resize_ratio) 

#cv2.imwrite("tc_img_sized.png", tc_img_sized)

#l_img = cv2.flip(cv2.imread("thumb_01.png"), -1)
#s_img = cv2.flip(tc_img_sized, -1)

#x_offset = y_offset = 0
#l_img[y_offset: s_img.shape[0], x_offset: s_img.shape[1]] = s_img

#l_img = cv2.flip(l_img, -1)
#cv2.imwrite("tc_img_w_tc.png", l_img)


#l_img = cv2.imread("thumb_01.png")

#vidCap = cv2.VideoCapture("big_buck_bunny.mp4")

#x_offset = y_offset = 2
#l_img[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img

#cv2.imwrite("aaaaa.png", l_img)
