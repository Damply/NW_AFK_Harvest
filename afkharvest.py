from re import purge
import keyboard
import mss
import cv2
import pyautogui
import numpy
from time import time, sleep
import random, threading
from threading import Thread
import os

pyautogui.PAUSE = 0


print("Damply's afk auto harvest")


print("Press 's' to start playing.")
print("Once started press 'z' to quit.")
keyboard.wait('s')


def harvest():	
	sct = mss.mss()
	dimensions_left = {
			'left': 740,
			'top': 350,
			'width': 400,
			'height': 400
		}

	red_img = cv2.imread('e.png', cv2.IMREAD_UNCHANGED)
	w = red_img.shape[1]
	h = red_img.shape[0]
	threshold = .80
	
	while True:
		scr = numpy.array(sct.grab(dimensions_left))
		scr2 = numpy.array(sct.grab(dimensions_left))
	
		result = cv2.matchTemplate(scr, red_img, cv2.TM_CCOEFF_NORMED)
		min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
		yloc, xloc = numpy.where(result >= threshold)
		for (x, y) in zip(xloc, yloc):
			pyautogui.press("E")
		
		cv2.imshow('Game', scr)
		cv2.waitKey(1)
		if keyboard.is_pressed('z'):
			os._exit(0)
			
			
def afk():
	while True:
		time_out_time = random.randint(25,120)			
		sleep(time_out_time)
		pyautogui.press("space")
		

	
t1 = threading.Thread(target=harvest)
t2 = threading.Thread(target=afk)

t1.start()
t2.start()
t1.join()
t2.join()