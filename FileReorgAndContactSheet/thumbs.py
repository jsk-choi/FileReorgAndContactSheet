import os
import sys
import cv2
import collections

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.path.append("..{0}FileReorg".format(os.path.sep))

from ClassFileInfo import *

import Capture as cap
import Config as conf
import FileSystem as fs	
import Functions as fn
import Image as img
import Print as prn

if (len(sys.argv) > 1) and os.path.isdir(sys.argv[1]):
	conf.paths = [sys.argv[1].strip()]

for dir in conf.paths:

	files = list(fs.GetAllFiles(dir))

	for file in files:

		file_info = FileInfo(file, dir)

		if file_info.extension in conf.video_ext:

			if not fn.CorrespondingContactSheetExists(os.path.join(file_info.folder, fs.FileNameOnly(file_info.filename)), conf.contact_ext, files):

				try:
					img.create_contact_sheet(file_info.fullfilename)
				except:
					prn.print_("Error: " + str(sys.exc_info()[1]))
					prn.print_("\n\n")
