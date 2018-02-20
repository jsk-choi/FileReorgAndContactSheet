import os
import sys

from classes import *
import file_system as fs
import imaging as img
import rtconfig as cf
import rtfunctions as fn
import rtprint as pr

if (len(sys.argv) > 1) and os.path.isdir(sys.argv[1]):
	cf.paths = [sys.argv[1].strip()]
else:
	pr.print_("Supplied path not recognized as a valid folder: {0}".format(sys.argv[1]))
	sys.exit()

for dir in cf.paths:

	files = list(fs.get_all_files(dir))

	for file in files:

		file_nfo = file_info(file, dir)

		if file_nfo.extension in cf.video_ext:

			if not fn.CorrespondingContactSheetExists(os.path.join(file_nfo.folder, fs.FileNameOnly(file_nfo.filename)), cf.contact_ext, files):

				try:
					img.create_contact_sheet(file_nfo.fullfilename)
				except:
					pr.print_("Error: {0}{1}{1}".format(str(sys.exc_info()[1]), "\n"))
