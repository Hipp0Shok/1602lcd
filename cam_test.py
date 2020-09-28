BUTTON_PIN = 14

import cv2
import lcddriver

import sys
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
lcd = lcddriver.lcd()
cam = cv2.VideoCapture(0)

print("push 3 times")
click_cnt = 0
while click_cnt < 3:
	inputValue = GPIO.input(BUTTON_PIN)
	if(inputValue == True):
		click_cnt = click_cnt + 1
		print(click_cnt)
	sleep(10)
lcd.lcd_display_string("Show your sign", 1)
while(True):
    ret, img = cam.read()
    cv2.imshow('my_cam', img)
    if cv2.waitKey(10) == 27:
	    break
cam.release()
cv2.destroyAllWindows()

cam.release()
cv2.destroyAllWindows()
print("done")
GPIO.cleanup()
