import collections

import Config as conf
import Classes as cl
import Image as img

def capture_thumbnails(filename):
	# open the video file
	vid_attr = cl.vid_attr(filename, conf.thumbs_horizontal, conf.thumbs_vertical, conf.video_pad)

	# starting frame
	frame_counter = vid_attr.startframe

	thumbs_dict = {}
	success = True

	for ii in range(1, vid_attr.totalthumbs + 1):

		# jump to frame, capture frame
		vid_attr.vid_cap.set(1, frame_counter)
		success, frame = vid_attr.vid_cap.read()

		if success:
			# overlay timecode
			thumbs_dict[frame_counter] = img.overlay_timecode_on_thumbnail(int(frame_counter / vid_attr.fps), frame)
			# move frame location forward
			frame_counter += vid_attr.frameinterval
		else:
			break

	# return dict in key ordered
	return collections.OrderedDict(sorted(thumbs_dict.items()))
