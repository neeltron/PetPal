# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 01:47:04 2021

@author: Neel
"""

from picamera import PiCamera
from time import sleep

live = PiCamera()
live.rotation = 180

live.start_preview()
sleep(5)
i = 1

while True:
    i = i + 1
    live.capture('liveimage' + i + '.jpg')
    sleep(10)
