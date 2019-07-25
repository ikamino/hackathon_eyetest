'''
THIS IS THE FINAL CODE FOR THE PROJECT
CODE FOR ALARM: 
    import winsound 
    duration = 1000
    freq = 440
    winsound.Beep(freq, duration)
    print ('\007') OR print('\a')
'''




import requests
import cv2
import numpy as np
import os
import time
import json
import urllib.request
import urllib.parse
import base64
import glob

subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

'''
real time record video off of camera then parse video into individual frames
clientID: a230297bd00d52a
clientSecret: 0cb3594114f3a9bb95e2271d772c5261276d9b23
'''
'''
def imgur(name):
    f = open(name, "rb")
    image_data = f.read()
    headers = {'Authorization': 'Client-ID ' + client_id}
    data = {'image': base64.standard_b64encode(image_data), 'title': 'test'} # create a dictionary.
    request = urllib.request.Request(url="https://api.imgur.com/3/upload.json", data=urllib.parse.urlencode(data).encode("utf-8"),headers=headers)
    response = urllib.request.urlopen(request).read()
    parse = json.loads(response)
    parse2 = parse['data']['link']
    #print (parse['data']['link'])
    return parse2

client_id = 'a230297bd00d52a'
'''
#os_type = int (input('press 0 if you only have a front camera and 1 if you have a front and back camera '))
'''
if os_type == 0: 
    print ("Are you sure you only have a front camera? type 'y' for yes and 'n' for no")
elif os_type == 1: 
    print ("Are you sure you have a front and back camera? type 'y' for yes and 'n' for no")
verifying_type = str(input(' '))
#recording video
'''

def all():
    
    if os.path.exists('data') == True:
            remove_data = glob.glob("./data/*")
            for r in remove_data:
                os.remove(r)
    else:
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print ('Error: Creating directory of data')
            
        
    
    start = time.time()
    currentFrame = 0
    cap = cv2.VideoCapture(1) 
    
    #album = []
    while (cap.isOpened()):
        ret, frame = cap.read()
        if (time.time() - start) > 3:
            name = './data/frame' + str(currentFrame) + '.png'
            #print ('Creating...' + name)
            cv2.imwrite(name, frame)
            #url_return = imgur(name)
            #print (url_return)
            #album.append(url_return)
            #print (album)
            #os.remove(name)
            start = time.time()
        cv2.imshow('name', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        currentFrame += 1
    # Stop recording
    cap.release()
    cv2.destroyAllWindows()
    currentFrame = 0
    
    #print (os.listdir('./data'))
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text = "Start", 
                   fg="red", 
                   command= all
                   )
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, 
                   text = "Stop",
                   command = quit)
slogan.pack(side=tk.RIGHT)
root.mainloop()
