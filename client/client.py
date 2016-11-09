import cv2
import requests
import base64

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    cv2.imwrite("temp.jpg",frame)
    temp=open("temp.jpg","rb")
    binary=temp.read()
    response=requests.post("http://127.0.0.1:5000/upload", data=base64.b64encode(binary))