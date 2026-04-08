import Rpi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

botton = 13
GPIO.setup(button, GPIO.IN)

state = 0

while True:
    if GPIO.input(button)
    state = not state
    GPIO.output(led, state)
    time.sleep(0.2)

