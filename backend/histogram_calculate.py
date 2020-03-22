import cv2
import os
from matplotlib import pyplot as plt
import shutil

try:
  os.mkdir('Histograms')
except:
  shutil.rmtree('Histograms')
  os.mkdir('Histograms')

for img_name in os.listdir('Segments'):
  img = cv2.imread('Segments/'+img_name)
  print(img_name)
  color = ('b','g','r')
  for i,col in enumerate(color):
    histr = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,255])
    plt.ylim([0,500])
  plt.savefig('Histograms/'+img_name.replace('jpg','png'))
  plt.close()