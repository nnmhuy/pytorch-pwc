import numpy as np
import cv2

cap = cv2.VideoCapture('./videos/1.mp4')
ret, currentFrame = cap.read()

while(cap.isOpened()):
  ret, nextFrame = cap.read()
  cv2.imwrite('./images/first.png', currentFrame)
  cv2.imwrite('./images/second.png', nextFrame)
  currentFrame = nextFrame


cap.release()
