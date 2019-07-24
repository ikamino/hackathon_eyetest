
'''
real time record video off of camera then parse video into individual frames
clientID: a230297bd00d52a
clientSecret: 0cb3594114f3a9bb95e2271d772c5261276d9b23
'''
import cv2
import numpy as np
import os
import time
import glob

if not os.path.exists('data') == False:
    clr_data = glob.glob('./data/*')
    for d in clr_data: 
        os.remove(d)
else:
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print ('Error: Unable to create folder for data storage')
#determine whether to capture images with front or back camera
os_type = int (input('press 0 if you only have a front camera and 1 if you have a front and back camera '))
if os_type == 0: 
    print ("Are you sure you only have a front camera? type 'y' for yes and 'n' for no")
elif os_type == 1: 
    print ("Are you sure you have a front and back camera? type 'y' for yes and 'n' for no")
verifying_type = str(input(' '))
#recording video
if verifying_type == 'y': 
    start = time.time() + 3
    currentFrame = 0
    cap = cv2.VideoCapture(os_type) 
    while time.time() <= start:
        ret, frame = cap.read()
        name = './data/frame' + str(currentFrame) + '.png'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
        currentFrame += 1
    # When everything done, release the capture
cv2.destroyAllWindows()
cap.release()
if verifying_type == 'n': 
        print ('refresh program')

#cv2.destroyAllWindows()'''