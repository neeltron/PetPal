# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 01:47:04 2021

@author: Neel
"""

from picamera import PiCamera
from time import sleep

live = PiCamera()

live.start_preview()
sleep(5)
live.stop_preview()
