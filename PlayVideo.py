video_path = r"C:\Users\Administrator\Videos\video.mp4"
imgwindow = "Sorting"
import cv2
import numpy as np
from pygame import mixer
mixer.init()
mixer.music.load(r"C:\Users\Administrator\Videos\audio.mp3")
  
# Create a VideoCapture object and read from input file
cv2.namedWindow(imgwindow, cv2.WINDOW_AUTOSIZE)
cap = cv2.VideoCapture(video_path)
mixer.music.play()
  
# Check if camera opened successfully 
if (cap.isOpened()== False): 
    print("Error opening video file") 
  
# Read until video is completed 
while(cap.isOpened()): 
      
# Capture frame-by-frame 
    ret, frame = cap.read() 
    if ret == True: 
    # Display the resulting frame 
        cv2.imshow(imgwindow, frame) 
          
        if cv2.waitKey(31) & 0xFF == ord('*'): 
            break
  
# Break the loop 
    else: 
        break
  
# When everything done, release 
# the video capture object 
cap.release() 
  
# Closes all the frames 
cv2.destroyAllWindows() 
