import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26

GPIO.setup(led, GPIO.OUT)

photo_res = 6

GPIO.setup(photo_res, GPIO.IN)

while True:
    GPIO.output(led, not GPIO.input(photo_res))
