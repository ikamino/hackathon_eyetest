import json
import urllib.request
import urllib.parse
import base64
import time


currentFrame = 0 
start = time.time()
start2 = time.time() + 0.1
client_id = 'a230297bd00d52a'
x = 0
for x in range(13):
    f = open("frame" + str(currentFrame) + ".png", "rb")
    image_data = f.read()
    b64_image = base64.standard_b64encode(image_data)
    headers = {'Authorization': 'Client-ID ' + client_id}
    data = {'image': b64_image, 'title': 'test'} # create a dictionary.
    request = urllib.request.Request(url="https://api.imgur.com/3/upload.json", data=urllib.parse.urlencode(data).encode("utf-8"),headers=headers)
    response = urllib.request.urlopen(request).read()
    parse = json.loads(response)
    print (parse['data']['link'])
    currentFrame += 1 
    x += 1