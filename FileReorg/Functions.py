
def CorrespondingVideoFileExists(cs_fn, vid_exts, all_files):	
	for ext in vid_exts:
		if (cs_fn + ext) in all_files:
			return True

	return False
