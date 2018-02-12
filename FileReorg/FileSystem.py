import os
from glob import glob

def GetAllFiles(rootPath):
	return [y for x in os.walk(rootPath) for y in glob(os.path.join(x[0], '*.*'))]

def FileExt(filePath):
	filename, file_extension = os.path.splitext(filePath)
	return file_extension

def FileNameOnly(filePath):
	filename, file_extension = os.path.splitext(filePath)
	return filename

def DeleteFile(filePath):
	os.remove(filePath)
	print('del:\t' + filePath)

def Movefile(src, dest):
	os.rename(src, dest)
	print('move:\t' + src + '\n\t' + dest)
