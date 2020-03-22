import os
import shutil
import cv2

res=[]
segments=[]
with open('Results.txt','r') as r:
  res=r.readlines()
for r in res:
  s=r.replace(':','').replace(',','').split()
  segments.append({s[0]:s[1],s[2]:float(s[3]),s[4]:int(s[5]),s[6]:int(s[7]),s[8]:int(s[9]),s[10]:int(s[11])})

try:
  os.mkdir('Segments')
except:
  shutil.rmtree('Segments')
  os.mkdir('Segments')

for i in range(len(segments)):
  s=segments[i]
  f=s['Prediction']+'_'+str(i)+'.jpg'
  img = cv2.imread('Extracted_Fruits/'+f)
  s=segments[i]
  print(s)
  # Cropping
  crop_img = img[s['y_min']:s['y_max'], s['x_min']:s['x_max']]
  # Shape returns Image Dimensions in (Height,Width) Format
  print('Cropped Dimensions : ',crop_img.shape)
  #Resizing
  h=crop_img.shape[0]
  w=crop_img.shape[1]
  width = 200
  height = 200
  if h>w:
    width = (200*w)//h
  elif w>h:
    height = (200*h)//w
  dim = (width, height)
  resized_img = cv2.resize(crop_img, dim, interpolation = cv2.INTER_AREA)
  print('Resized Dimensions : ',resized_img.shape)
  cv2.imwrite("Segments/"+f, resized_img);