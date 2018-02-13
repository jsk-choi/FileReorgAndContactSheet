import os
import shutil
import sys

import Config as conf
import FileSystem as fs
import Functions as fn
from ClassFileInfo import *

config = {}

def RenameMove(workingdir):

	# rename video file name and move to parent
	allfiles = fs.GetAllFiles(workingdir)

	# move video files to working folder root
	for file in allfiles:

		# object to parse out file path parts
		fileinfo = FileInfo(file, workingdir)

		if not fileinfo.isvalid: continue

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
		if not ExcludeInFileReorg(dir):
			shutil.rmtree(os.path.join(conf.GetConfig()['paths'][0], dir))


def DeleteUnwatedFiles(workingdir):

	config = conf.GetConfig()
	vid_exts = config['video-ext']
	cs_ext = config['contact-ext']

	allfiles = fs.GetAllFiles(workingdir)

	# delete unwanted files
	for file in allfiles:
	
		fileinfo = FileInfo(file, workingdir)

		if (not fileinfo.isvalid): continue

		# if contact sheet
		if (fileinfo.extension == cs_ext):
		# make sure matching video file exists
			if not CorrespondingVideoFileExists(fs.FileNameOnly(file), vid_exts, allfiles):
				# if no matching video file, delete
				fs.DeleteFile(file)
		# if is not contact sheet or video file, delete
		elif (fileinfo.extension not in vid_exts) or ('sample' in fileinfo.filename.lower()):
			fs.DeleteFile(file)


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

def getopts(argv):

	opts = {}  # Empty dictionary to store key-value pairs.

	try:
		while argv:  # While there are arguments left to parse...
			if argv[0][0] == '-':  # Found a "-name value" pair.
				opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
			argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
	except:
		help()

	if not bool(opts): 
		help()
		return (False, opts)

	return (bool(opts), opts)

def help():
	prompt = '\n'
	prompt += 'Required arguments:\n'
	prompt += '-r: omit = 0, reorg = 1\n'
	prompt += '  reorganize, moves files to root directory\n'
	prompt += '  renames file to parent directory name\n'
	prompt += '-p: [path]\n'
	prompt += '  path to directory to be reorganized\n\n'
	prompt += 'sample:'
	prompt += '  -a 1 -p \\\\nas\\files\\videos\n\n'
	print prompt