import cv2
import tensorflow as tf
import numpy as np
data_dir='/home/fan/Desktop/Fan/pose/data/OneDrive_1_2020-03-05/E_ID5/Es1/Raw/depth271114_114715.avi'
csv_dir='/home/fan/Desktop/Fan/pose/data/OneDrive_1_2020-03-05/E_ID5/Es1/Raw/JointPosition271114_114715.csv'

import csv

with open(csv_dir) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if(len(row)>1):
            line_count+=1


    print('Processed {line_count} lines.', line_count)

cap = cv2.VideoCapture(data_dir)
line_count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    line_count += 1
    if ret:
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

print(line_count)
cap.release()
cv2.destroyAllWindows()



