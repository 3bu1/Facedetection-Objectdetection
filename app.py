from darkflow.net.build import TFNet
import cv2
import sys
from PIL import Image
import urllib.request as urllib
import numpy as np
options = {
"model": "cfg/tiny-yolo-voc-3bu1.cfg",
 "load": 6000,
  "threshold": 0.1
  }
tfnet = TFNet(options)
personSeen = 0
print("above while")
stream=urllib.urlopen("http://192.168.0.25:8080/video")
bytes=bytes()
while True:
   bytes+=stream.read(1024)
   a = bytes.find(b'\xff\xd8')
   b = bytes.find(b'\xff\xd9')
   if a!=-1 and b!=-1:
       jpg = bytes[a:b+2]
       bytes= bytes[b+2:]
       i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
       #cv2.imshow('i', i)
       print("before tfnet: ")
       #curr_img_cv2 = cv2.cvtColor(i, cv2.COLOR_RGB2BGR)
       result = tfnet.return_predict(i)
       print(result)
       for detection in result:
        print("in if detection: ")
        print(detection['label']+str(detection['confidence']))
        if detection['label']=='tribhuvan' and detection['confidence']>0.25:
         print(detection['label']+str(detection['confidence']))
         print("person detected")
         personSeen += 1
        else:
         print("in else")
    #curr_img.save('birds/%i.jpg' % birdsSeen)
