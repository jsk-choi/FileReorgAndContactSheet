# reorg config
reorg_paths = [r'C:\Users\jchoi\Desktop\wip\py\fs sf']
thumb_paths = [r'C:\Users\jchoi\Desktop\wip\py\fs sf']
video_ext = [".mkv", ".flv", ".avi", ".mov", ".wmv", ".mp4", ".mpg", ".mpeg", ".m2v", ".m4v"]
contact_ext = ".png"
exclude_postfix = "-zz"
reorg = True

# thumbs config
width = 2500
thumbs_horizontal = 6
thumbs_vertical = 5
video_pad = 0.05
background_color = (244, 66, 232)
text_font = "courbd.ttf"
text_font_size = 25
thumb_spacing = 10
thumb_width = int(round((long(width) - ((thumbs_horizontal * thumb_spacing) + thumb_spacing)) / thumbs_horizontal))
thumb_height = 0

# output
out_message = []

# test reorg and thumb create results
debug = False