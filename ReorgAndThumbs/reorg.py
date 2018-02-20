import os
import sys

import rtconfig as cf
import rtfunctions as fn
import rtprint as pr

# handle if folder path is passed in
if (len(sys.argv) > 1) and os.path.isdir(sys.argv[1]):
	cf.paths = [sys.argv[1].strip()]
	pr.print_("Folder: " + sys.argv[1])
	resp = raw_input("Reorganize folder? (y/n): ")
	pr.print_("")
	cf.reorg = resp.strip().lower() == "y"
else:
	pr.print_("Parameter not recognized as folder, exiting")

# delete unwanted files
for dir in cf.paths:
	
	fn.DeleteUnwatedFiles(dir)

	if cf.reorg:
		fn.RenameMove(dir)
