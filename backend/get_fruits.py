import os
import shutil
import cv2
import numpy as np
from matplotlib import pyplot as plt

try:
  os.mkdir('Extracted_Fruits')
except:
  shutil.rmtree('Extracted_Fruits')
  os.mkdir('Extracted_Fruits')
img = cv2.imread("detect_fruits.jpg")

res=[]
segments=[]
with open('Results.txt','r') as r:
  res=r.readlines()
for r in res:
  s=r.replace(':','').replace(',','').split()
  segments.append({s[0]:s[1],s[2]:float(s[3]),s[4]:int(s[5]),s[6]:int(s[7]),s[8]:int(s[9]),s[10]:int(s[11])})
  
for i in range(len(segments)):
  s=segments[i]
  img = cv2.imread('detect_fruits.jpg')
  mask = np.zeros(img.shape[:2],np.uint8)
  bgdModel = np.zeros((1,65),np.float64)
  fgdModel = np.zeros((1,65),np.float64)
  rect=(s['x_min'],s['y_min'],s['x_max'],s['y_max'])
  cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
  mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
  img = img*mask2[:,:,np.newaxis]
  cv2.imwrite("Extracted_Fruits/"+s['Prediction']+"_"+str(i)+'.jpg', img)