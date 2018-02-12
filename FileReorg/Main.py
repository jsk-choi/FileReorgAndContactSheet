import shutil
import glob

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

# move video files to working folder root
for file in allfiles:

	# object to parse out file path parts
	fileinfo = FileInfo(file, conf.GetConfig()['paths'][0])

	# skip file is not video or marked for omit reorg
	if (fileinfo.extension not in conf.GetConfig()["video-ext"]) or fileinfo.isatroot or fileinfo.excludefilereorg: continue

	# unique counter 
	iterator = 0
	newfilename = os.path.join(fileinfo.rootfolder, fileinfo.parentfoldername) + fileinfo.extension

	# make filename unique if exists in destination
	while os.path.isfile(newfilename):
		newfilename = os.path.join(fileinfo.rootfolder, fileinfo.parentfoldername) + "-" + ("%02d" % (iterator,)) + fileinfo.extension
		iterator += 1

	# move / rename file to parent root dir
	fs.Movefile(fileinfo.fullfilename, newfilename)
	
# delete subdirs

# get first level subdirs
subdirs = next(os.walk(conf.GetConfig()['paths'][0]))[1]

# delete dir is not omit reorg
for dir in subdirs:
	if not fn.ExcludeInFileReorg(dir):
		shutil.rmtree(os.path.join(conf.GetConfig()['paths'][0], dir))
