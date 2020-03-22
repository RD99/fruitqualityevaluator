import cv2
import shutil
import os

try:
  os.mkdir('Edge_Detect')
except:
  shutil.rmtree('Edge_Detect')
  os.mkdir('Edge_Detect')

for img_name in os.listdir('Segments'):
  img = cv2.imread("Segments/" + img_name)
  edges = cv2.Canny(img,100,255)
  
  contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
  print("Number of Contours found = " + str(len(contours)))
  
  cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
  
  cv2.imwrite("Edge_Detect/" + img_name, img)
