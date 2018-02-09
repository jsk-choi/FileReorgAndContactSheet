import Config as conf
import FileSystem as fs
import Functions as fn

config = conf.GetConfig()
vid_exts = config['video-ext']
cs_ext = config['contact-ext']

allfiles = fs.GetAllFiles(config['paths'][0])

# delete unwanted files
for file in allfiles:
    # if contact sheet
    if (fs.FileExt(file) == cs_ext):
        # make sure matching video file exists
        if not fn.CorrespondingVideoFileExists(fs.FileNameOnly(file), vid_exts, allfiles):
            # if no matching video file, delete
            fs.DeleteFile(file)
    # if is not contact sheet or video file, delete
    elif fs.FileExt(file) not in vid_exts:
        fs.DeleteFile(file)

# rename video file name and move to parent



'''
1. get all files
2. delete files that are not video or contact sheet
3. 
'''