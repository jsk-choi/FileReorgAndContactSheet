import os

import rtprint as pr

def get_all_files(dir):
	walk = os.walk(dir)
	for folder in walk:
		for file in folder[2]:
			yield os.path.join(folder[0], file)

def file_ext(file_path):
	filename, file_extension = os.path.splitext(file_path)
	return file_extension

def filename_only(file_path):
	filename, file_extension = os.path.splitext(file_path)
	return filename

def delete_file(file_path):
	os.remove(file_path)
	pr.print_('del:\t' + file_path)

def move_file(src, dest):
	os.rename(src, dest)
	pr.print_(''.join(['move:\t', src, ' -->\n\t', dest]))
