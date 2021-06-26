# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 01:47:04 2021

@author: Neel
"""

from picamera import PiCamera
from time import sleep
import base64
import requests

live = PiCamera()
live.rotation = 180

live.start_preview()
sleep(5)

while True:
    live.capture('liveimage.jpg')
    sleep(10)
    with open("liveimage.jpg", "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": "4e8e6f9baef8b46f75ac078d4bded8c1",
            "image": base64.b64encode(file.read()),
        }
        res = requests.post(url, payload)
        dict = res.json()
        url = dict['data']['url']
