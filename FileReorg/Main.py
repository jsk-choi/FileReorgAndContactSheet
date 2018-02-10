import Config as conf
import FileSystem as fs
import Functions as fn
from ClassFileInfo import *

config = conf.GetConfig()
vid_exts = config['video-ext']
cs_ext = config['contact-ext']

allfiles = fs.GetAllFiles(config['paths'][0])

# delete unwanted files
for file in allfiles:
	
	fileinfo = FileInfo(file, conf.GetConfig()['paths'][0])

    # if contact sheet
	if (fileinfo.extension == cs_ext):
        # make sure matching video file exists
		if not fn.CorrespondingVideoFileExists(fs.FileNameOnly(file), vid_exts, allfiles):
            # if no matching video file, delete
			fs.DeleteFile(file)
    # if is not contact sheet or video file, delete
	elif (fileinfo.extension not in vid_exts) or ('sample' in fileinfo.filename.lower()):
		fs.DeleteFile(file)

# rename video file name and move to parent
allfiles = fs.GetAllFiles(config['paths'][0])

# delete unwanted files
for file in allfiles:
	
	fileinfo = FileInfo(file, conf.GetConfig()['paths'][0])

	if fileinfo.isatroot or fileinfo.excludefilereorg: continue

	uniqueiterator = ''
	iterator = 0

	newfilename = os.path.join(fileinfo.rootfolder, fileinfo.folder) + fileinfo.extension

	while os.path.isfile(newfilename):
		iterator += 1
		newfilename = os.path.join(fileinfo.rootfolder, fileinfo.parentfoldername) + ("%02d" % (iterator,)) + fileinfo.extension
	
	fff = fileinfo


#'''
#1. get all files
#2. delete files that are not video or contact sheet
#3. 
#'''