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

subscription_key = 'ffb1c11d2a624e4e8ba551f1b7a5349e'
assert subscription_key

'''
real time record video off of camera then parse video into individual frames
clientID: a230297bd00d52a
clientSecret: 0cb3594114f3a9bb95e2271d772c5261276d9b23
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
os_type = int (input('press 0 if you only have a front camera and 1 if you have a front and back camera '))
if os_type == 0: 
    print ("Are you sure you only have a front camera? type 'y' for yes and 'n' for no")
elif os_type == 1: 
    print ("Are you sure you have a front and back camera? type 'y' for yes and 'n' for no")
verifying_type = str(input(' '))
#recording video
'''
start = time.time() + 6
currentFrame = 0
cap = cv2.VideoCapture(0) 
album = []
while time.time() <= start:
    ret, frame = cap.read()
    name = './frame' + str(currentFrame) + '.png'
    #print ('Creating...' + name)
    cv2.imwrite(name, frame)
    url_return = imgur(name)
    #print (url_return)
    album.append(url_return)
    #print (album)
    os.remove(name)
    currentFrame += 1
# Stop recording
cv2.destroyAllWindows()
cap.release()
'''--------------------------------------------------------------------EYELID.PY------------------------------------------------------------------------------'''
face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'


control = ['https://cdn.discordapp.com/attachments/413154933278507008/603706754961899550/20190724_145400_HDR.jpg']
images = album
headers = {'Ocp-Apim-Subscription-Key': subscription_key}



params = { 
    'returnFaceId': 'flase',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'glasses'  
}

# imgur to azure
# imgurResp = request.post("imgururl", data={"image": file.read(path)})
# request.post("azureurl", data={"url": imgurResp.json()["url"]})
image_diffs = []
for image in control:

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image})



    data = response.json()
    face_data = data[0]
    # print (data)
    faceLandmarks = (face_data['faceLandmarks'])



    eyeLeftTop = faceLandmarks['eyeLeftTop']
    eyeLeftBottom = faceLandmarks['eyeLeftBottom']

   

    y1 = (eyeLeftTop['y'])
    y2 = (eyeLeftBottom['y'])

    control_value = y2-y1
    image_diffs.append(control_value)
   
for image in images: 
    if image != len(images):
        response = requests.post(face_api_url, params=params,
                                headers=headers, json={"url": image})
    
        data = response.json()
        face_data = data[0]
        faceLandmarks = (face_data['faceLandmarks'])
    
        eyeLeftTop = faceLandmarks['eyeLeftTop']
        eyeLeftBottom = faceLandmarks['eyeLeftBottom']
    
        y1 = (eyeLeftTop['y'])
        y2 = (eyeLeftBottom['y'])
    
        differences = y2-y1
        image_diffs.append(differences)
    
        terms_in_diffs = len(image_diffs)
    else: 
        break


# print('Open Values: ', open_list)
# print('Close List: ' , close_list)

# #number of terms in each list
# count_open_list = len(open_list) 
# count_close_list = len(close_list)

# print("\n \n")
# print('There are ', count_open_list, ' terms in the open list.')
# print('There are ', count_close_list, ' terms in the close list.')


i = 0
place = 0
closed_times = []
test = []
custom_control = (control_value - 20)
for b in range (i, terms_in_diffs):
    if image_diffs[place] < (custom_control):
        closed_times.append('closed')
        if len(closed_times) >= 3:
            print('help')
            break
        place += 1

    elif image_diffs[place] >= custom_control:
        test.append('open')
        del (closed_times[0:len(closed_times)])
        place += 1
    


print (image_diffs)
print (len(test))
