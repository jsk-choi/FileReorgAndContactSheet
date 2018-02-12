import os
import Config as conf

def CorrespondingVideoFileExists(cs_fn, vid_exts, all_files):

	for ext in vid_exts:
		if (cs_fn + ext) in all_files:
			return True

	return False

def CorrespondingContactSheetExists(vid_fn, cs_ext, all_files):

	if (vid_fn + cs_ext) in all_files:
		return True

	return False

def ExcludeInFileReorg(vid_fn):	

	fullpath = vid_fn.split(os.sep)
	excludepattern = conf.GetConfig()['exclude-postfix']

	for item in fullpath:
		if item.endswith(excludepattern):
			return True

	return False
