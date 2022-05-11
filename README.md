# video-slide-maker.py
This takes an mp4 video file and makes unique jpg slides.

This file will take an mp4 file and make a series of jpg image files.  It is intended that if you have a video power point presentation but have lost the power point slides it attempts to capture them from the video.

The command is `slideMaker.py "yourVideo.mp4"` and this will create a folder called yourVideo_slides and in them will be jpg slides.  To run from command line, the slideMaker.py must be in the same directory where the terminal is running, it is not globally installed on the system.  I also locate the video in the same folder for simplicity, otherwise you would have to specify full or relative path.

Or if you run it without an argument, it will look for "test_video.mp4" in the current directory.

The way it works is by taking a snapshot of the video about every 5 seconds.  It looks to see if the new snapshot is similar.  If the new snapshot is similar, it does not save a new jpg.  If the new snapshot is different, it will save to a new jpg and increment the slide index.

It requires:
`Image from PIL, imagehash, os, cv2, and sys` as libraries.

The imagehash threshold can manually be changed in the source code.  0 is perfect match, 32 is no match, 64 is opposite.  So I set at 5 which seems to work ok.

### The following are references for how I developed this, and I did heavily borrow from these answers:

https://stackoverflow.com/questions/33311153/python-extracting-and-saving-video-frames
https://stackoverflow.com/users/6452438/yuchao-jiang

https://stackoverflow.com/questions/52736154/how-to-check-similarity-of-two-images-that-have-different-pixelization
https://stackoverflow.com/users/1977847/h%c3%a5ken-lid
