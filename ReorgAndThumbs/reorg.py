import os
import sys

import rtconfig as cf
import rtfunctions as fn
import rtprint as pr

import rtfilesys as fs
from rtclasses import *

dir = r"C:\Users\jchoi\Desktop\wip\py\fs sf"

#fff = [x[0] for x in os.walk(dir)]
fff = fs.get_all_subdir(dir)

for sub_dir in fff:
	print(sub_dir)
	print(file_info(sub_dir, dir).excludefilereorg)

for thing in fff:
	print(thing)

print('')

#fff.sort(key=len, reverse=True)

for thing in fff:
	print(thing)

#if cf.debug: pr.print_("Debug mode is on\n\n")

## handle if folder path is passed in
#if (len(sys.argv) > 1):
#	in_path = str(sys.argv[1]).strip().replace('"', '')
#	if os.path.isdir(sys.argv[1]):
#		cf.reorg_paths = [in_path]
#		pr.print_("Folder: " + in_path)
#		resp = raw_input("Reorganize folder? (y/n): ")
#		pr.print_("")
#		cf.reorg = resp.strip().lower() == "y"
#	else:
#		pr.print_("Parameter not recognized as folder, exiting")
#		sys.exit()

## delete unwanted files
#for dir in cf.reorg_paths:
	
#	fn.delete_unwanted_files(dir)

#	if cf.reorg:
#		fn.rename_move(dir)
