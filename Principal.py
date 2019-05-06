# -*- coding: utf-8 -*-
import cv2
from ProcuraThumbnail import ProcuraThumbnail
import math
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('Videos/Video7.mp4')
thumb = cv2.imread('Thumbnails/Thumbvideo7.jpg')
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

p = ProcuraThumbnail()
#thumbMod = p.limpaRuido(thumb)
contadorFrames = 0
tempo = 0
fps = cap.get(cv2.CAP_PROP_FPS)

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  contadorFrames += 1
  if ret == True:
      if (contadorFrames % round(fps) == 0): tempo += 1
      if (contadorFrames % 5 == 0):
          cv2.imshow('Frame',frame)
          if cv2.waitKey(25) & 0xFF == ord('q'):
              break
          if (p.procuraThumbnailTipo3(thumb, frame) == 1):
              minutos = tempo/60
              frac, whole = math.modf(minutos)
              cv2.imshow('achada em ' + str(math.trunc(whole)) + ' minuto e ' + str(math.trunc(frac*60)) + ' segundos.', frame)
              cv2.waitKey(0)
              break
      
 
    # Display the resulting frame
    #cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    #if cv2.waitKey(25) & 0xFF == ord('q'):
      #break
 
  # Break the loop
  else: 
    break
 
# When everything done, release the video capture object'''
cap.release()
