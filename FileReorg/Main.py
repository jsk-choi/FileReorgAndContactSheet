import os
import sys

import Config as conf
import Functions as fn

# delete unwanted files
for dir in conf.paths:
	
	fn.DeleteUnwatedFiles(dir)

	if conf.reorg:
		fn.RenameMove(dir)

