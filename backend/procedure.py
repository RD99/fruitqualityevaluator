import os
print('Predicting...')
os.system('python keras-yolo3/yolo_video.py --image')
print('\nExtracting Furits...')
os.system('python get_fruits.py')
print('\nCropping Fruits...')
os.system('python crop_fruits.py')
print('\nDrawing Histograms...')
os.system('python histogram_calculate.py')
print('\nPerforming Quality Check...')
os.system('python quality_check.py')