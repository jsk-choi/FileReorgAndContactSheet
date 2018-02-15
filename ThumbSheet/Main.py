import os
import sys
import Image

import cv2

s_img = Image.TimecodeImage(2974)
l_img = cv2.imread("thumb_01.png")
x_offset = y_offset = 2
l_img[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img

cv2.imwrite("aaaaa.png", l_img)
