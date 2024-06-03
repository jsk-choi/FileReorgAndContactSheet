# add . to extension if not exists
def add_period_ifnot_exists(ext):
    return ext.lower() if str(ext).startswith('.') else "." + ext.lower()

def calc_thumb_width():
    thumb_width = int(round((width * 1.0 - ((thumbs_columns * thumb_spacing) + thumb_spacing)) / thumbs_columns))
    return thumb_width

# reorg config
reorg_paths = [r'']
thumb_paths = [r'']
video_ext = [".mkv", ".flv", ".avi", ".mov", ".wmv", ".mp4", ".mpg", ".mpeg", ".m2v", "m4v"]
contact_ext = ".jpg"
exclude_postfix = "-zz"
reorg = True

# thumbs config
width = 3000
thumbs_columns = 5
thumbs_rows = 5

thumbs_columns_verticalvideo = 7
thumbs_rows_verticalvideo = 3
thumbs_columns_horizontalvideo = 5
thumbs_rows_horizontalvideo = 5

video_pad = 0.03
background_color = (244, 66, 232)
text_font = "courbd.ttf"
text_font_size = 25
thumb_spacing = 3
thumb_width = calc_thumb_width()
thumb_height = 0

# global
out_message = []
working_dir = ''

# test reorg and thumb create results
debug = False

# add . to extension if not exists
for ii in range(0, len(video_ext)):
    video_ext[ii] = add_period_ifnot_exists(video_ext[ii])

contact_ext = add_period_ifnot_exists(contact_ext)

