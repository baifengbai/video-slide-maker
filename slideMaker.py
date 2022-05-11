
from PIL import Image
import imagehash
import os
import cv2
import sys

if len(sys.argv)>1:
    videoFilename = sys.argv[1]
else:
    videoFilename = "test_video.mp4"
videoFilenameBase = videoFilename.split(".")[0]
videoFilenameExtension = "."+videoFilename.split(".")[1]
folder = videoFilenameBase + "_slides" 
try:
    os.mkdir(folder)
except:
    pass

# print(cv2.__version__)
vidcap = cv2.VideoCapture(videoFilenameBase+videoFilenameExtension)
fps= int(vidcap.get(cv2.CAP_PROP_FPS))
print("frames per second",fps)

def similarImage(image1Filename,image2Filename,cutoff):
    hash1 = imagehash.average_hash(Image.open(image1Filename))
    hash2 = imagehash.average_hash(Image.open(image2Filename))
    if hash1 - hash2 < cutoff:
        return True
    else:
        return False

count = 0
unique = 1
seconds = 5
frequency = seconds*fps
#read first frame
success, imageOld = vidcap.read()
oldFilename = os.path.join(folder,"slide{:d}.jpg".format(unique))
cv2.imwrite(oldFilename, imageOld)
print("made slide " + str(unique))
unique+=1 #increment
while True:
    success,imageNew = vidcap.read()
    if not success:
        break
    if count%frequency == 0: #snapshot every so many frames
        newFilename = os.path.join(folder,"slide{:d}.jpg".format(unique)) #already incremented
        cv2.imwrite(newFilename, imageNew)
        similar = similarImage(oldFilename,newFilename, 8)
        if similar==False: #new and different image!
            print("made slide " + str(unique) + " around " + str((count/fps)/60) + " minutes")
            unique +=1
            oldFilename=newFilename
    count += 1
    
print("{} images are extacted in {}.".format(unique-1,folder))




