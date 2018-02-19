import os
import sys
import cv2
import collections

import numpy as np
from PIL import Image, ImageDraw, ImageFont

import Functions as fn
import Capture as cap
import Config as conf
import ClassFileInfo
from ClassFileInfo import *
import Image as img
import Print as prn

import FileSystem as fs	

working_dir = r'C:\Users\jchoi\Desktop\wip\py'

files = list(fs.GetAllFiles(working_dir))

for file in files:
	file_info = FileInfo(file, working_dir)

	if file_info.extension in conf.video_ext:
		if not fn.CorrespondingContactSheetExists(os.path.join(file_info.folder, fs.FileNameOnly(file_info.filename)), conf.contact_ext, files):

			try:
				img.create_contact_sheet(file_info.fullfilename)
			except:
				prn.print_("Error: " + str(sys.exc_info()[1]))
				prn.print_("\n\n")
