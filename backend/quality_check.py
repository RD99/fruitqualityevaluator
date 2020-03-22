import cv2
import os
import shutil
from PIL import ImageFont
import numpy as np

def get_quality(f,per_r,per_y,per_g):
  fruit=''
  quality=''
  
  if 'Apple' in f:
    fruit='Apple'
    if per_g>per_r and per_g>per_y:
      quality='Raw'
    elif per_y>per_g and per_y>per_r:
      quality='Ripe'
    elif per_r>per_g and per_r>per_y:
      quality='Ripe, Top Quality'

  elif 'Banana' in f:
    fruit='Banana'
    if abs(per_g-per_r)<0.1:
      quality='Ripe'
    elif per_g>per_r and per_g>per_y:
      quality='Raw'

  elif 'Orange' in f:
    fruit='Orange'
    if per_g>per_r and per_g>per_y:
      quality='Raw'
    if per_r>per_g and per_y>per_g:
      quality='Ripe'

  elif 'Mango' in f:
    fruit='Mango'
    if per_g>per_r and per_g>per_y:
      quality='Raw'
    if per_r>per_g and per_y>per_g:
      quality='Ripe'
      
  elif 'Papaya' in f:
    fruit='Papaya'
    if per_g>per_r and per_g>per_y:
      quality='Raw'
    if per_r>per_g and per_y>per_g:
      quality='Ripe'
      
  return fruit,quality

try:
  os.mkdir('Evaluation')
except:
  shutil.rmtree('Evaluation')
  os.mkdir('Evaluation')

res=[]
segments=[]
with open('Results.txt','r') as r:
  res=r.readlines()
for r in res:
  s=r.replace(':','').replace(',','').split()
  segments.append({s[0]:s[1],s[2]:float(s[3]),s[4]:int(s[5]),s[6]:int(s[7]),s[8]:int(s[9]),s[10]:int(s[11])})

image = cv2.imread('detect_fruits.jpg')
colors=[(0,0,255),(0,255,0),(255,255,127),(255,255,0),(255,0,255),(0,255,255)]
with open('Predictions.txt','w') as writer:
  for i in range(len(segments)):
    s=segments[i]
    f=s['Prediction']+'_'+str(i)+'.jpg'
    img = cv2.imread('Segments/'+f)
    # cv2 reads in BGR
    r=0
    g=0
    y=0
    for row in img:
      for cell in row:
        pixel=[int(cell[0]),int(cell[1]),int(cell[2])]
        g+=pixel[1]
        y+=(pixel[1]+pixel[2])//2
        r+=pixel[2]
    total=r+y+g
    per_r=r/total
    per_y=y/total
    per_g=g/total
    print(f)
    print('Red:',r)
    print('Yellow:',y)
    print('Green:',g)
    print('Red Percentage:',per_r)
    print('Yellow Percentage:',per_y)
    print('Green Percentage:',per_g)
    fruit,qual=get_quality(f,per_r,per_y,per_g)
    print('Fruit:',fruit,'\nQuality Prediction:',qual)
    start_points='('+str(s['x_min'])+','+str(s['y_min'])+')'
    end_points='('+str(s['x_max'])+','+str(s['y_max'])+')'
    cv2.rectangle(image,(s['x_min'],s['y_min']),(s['x_max'],s['y_max']),colors[i%len(colors)],2)
    writer.write('Fruit:'+s['Prediction']+'  Bounding Box:'+start_points+','+end_points+'  Quality:'+qual+'\n')
    shutil.copyfile('Segments/'+f,'Evaluation/'+f.replace('.jpg','')+'_'+qual+'.jpg')
    label=fruit+': '+qual
    labelSize=cv2.getTextSize(label,cv2.FONT_HERSHEY_DUPLEX,0.75,2)
    # print('labelSize>>',labelSize)
    l_x1 = s['x_min']
    l_y1 = s['y_min']#+int(labelSize[0][1]/2)
    l_x2 = l_x1+labelSize[0][0]
    l_y2 = l_y1-int(labelSize[0][1])
    cv2.rectangle(image,(l_x1,l_y1),(l_x2,l_y2),colors[i%len(colors)],cv2.FILLED)
    cv2.putText(image,label,(s['x_min'],s['y_min']),cv2.FONT_HERSHEY_DUPLEX,0.75,(0,0,0),1)
    cv2.imwrite('Final_Evaluation.jpg',image)