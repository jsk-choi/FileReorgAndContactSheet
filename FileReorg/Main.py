import FileSystem as fs
import Config as conf
import Functions

config = conf.GetConfig()
vid_exts = config['video-ext']
cs_ext = config['contact-ext']

allfiles = fs.GetAllFiles(config['paths'][0])

for file in allfiles:
	if (fs.FileExt(file) == cs_ext):
		print Functions.CorrespondingVideoFileExists(fs.FileNameOnly(file), vid_exts, allfiles)

#	elif fs.FileExt(file) not in vid_exts:
#		#fs.DeleteFile(file)


'''
1. get all files
2. delete files that are not video or contact sheet
3. 
'''