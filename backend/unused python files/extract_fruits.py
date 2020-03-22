import cv2
import os
import shutil
import numpy as np

try:
  os.mkdir('Extracted')
except:
  shutil.rmtree('Extracted')
  os.mkdir('Extracted')

for img_name in os.listdir('Segments'):
    img = cv2.imread("Segments/" + img_name)
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.GaussianBlur(gray_img, (7, 7), 0)
    adapt_thresh_im = cv2.adaptiveThreshold(gray_blur, 100, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 20)
    max_thresh, thresh_im = cv2.threshold(gray_img, 0, 120, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    thresh = cv2.bitwise_or(adapt_thresh_im, thresh_im)
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    sure_bg = cv2.dilate(thresh,kernel,iterations=2)
    img[sure_bg == 0] = [0,0,0]
    cv2.imwrite("Extracted/" + img_name, img)