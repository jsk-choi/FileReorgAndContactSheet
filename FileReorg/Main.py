import sys

import Config as conf
import Functions as fn

vid_exts = config['video-ext']
cs_ext = config['contact-ext']

# delete unwanted files
for dir in config['paths']:
	fn.DeleteUnwatedFiles(dir)
	fn.RenameMove(dir)