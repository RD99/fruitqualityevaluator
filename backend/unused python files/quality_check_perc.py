import cv2
import os

for f in os.listdir('Extracted'):
  img = cv2.imread('Extracted/'+f)
  # cv2 reads in BGR
  r=0.0
  g=0.0
  y=0.0
  n=1
  for row in img:
    for cell in row:
      pixel=[int(cell[0]),int(cell[1]),int(cell[2])]
      t=pixel[1]+((pixel[1]+pixel[2])//2)+pixel[2]
      if pixel[2]>0:
        r+=pixel[2]/t
      if (pixel[1]+pixel[2])//2>0:
        y+=((pixel[1]+pixel[2])//2)/t
      if pixel[1]>0:
        g+=pixel[1]/t
    n+=1
  total=r+y+g
  per_r=r/total
  per_y=y/total
  per_g=g/total
  # print('Red:',r)
  # print('Yellow:',y)
  # print('Green:',g)
  # print('Red:',r/total)
  # print('Yellow:',y/total)
  # print('Green:',g/total)
  print(f)
  if per_g>per_r and per_g>per_y:
    print('Quality Prediction: Raw')
  elif per_y>per_g and per_y>per_r:
    print('Quality Prediction: Ripe')
  elif per_r>per_g and per_r>per_y:
    print('Quality Prediction: Ripe, Top Quality')