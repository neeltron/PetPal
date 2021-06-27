# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 01:47:04 2021

@author: Neel
"""

import cv2
from time import sleep
import base64
import requests
import serial

temperature = serial.Serial('COM5')
temperature.flushInput()

cam = cv2.VideoCapture(0)

while True:
    try:
        temp = temperature.readline()
        decoded = float(temp[0:len(temp)-2].decode("utf-8"))
        print(decoded)
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        cv2.imwrite("liveimage.jpg", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            with open("liveimage.jpg", "rb") as file:
                url = "https://api.imgbb.com/1/upload"
                payload = {
                    "key": "4e8e6f9baef8b46f75ac078d4bded8c1",
                    "image": base64.b64encode(file.read()),
                }
                res = requests.post(url, payload)
                dict = res.json()
                url = dict['data']['url']
    except:
        print("error")
