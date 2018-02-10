import os
import Config as conf
import FileSystem as fs
import Functions as fn

class FileInfo:

	def __init__(self, fullpath, workingfolder):

		if not os.path.isfile(fullpath):
			raise ValueError('Not a file: ' + fullpath)

		filenameArr = fullpath.split(os.sep)

		self.rootfolder = workingfolder
		self.fullfilename = fullpath
		self.filename = filenameArr[-1]
		self.extension = fs.FileExt(fullpath); 
		self.folder = os.sep.join(filenameArr[:-1])
		self.excludefilereorg = fn.ExcludeInFileReorg(self.fullfilename)

		self.isatroot = self.rootfolder == self.folder;
		if self.isatroot: return
		
		parentArr = fullpath.replace(workingfolder, "").split(os.sep)
		
		self.parentfoldername = [s for s in parentArr if len(s) > 0][0]
		
		workingfolderArr = [s for s in workingfolder.split(os.sep) if len(s) > 0]
		workingfolderArr.append(self.parentfoldername)

		self.parentfolderpath = os.sep.join(workingfolderArr)
