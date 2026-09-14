from gpiozero import PWMLED
from time import sleep

red = PWMLED(17)
yellow = PWMLED(27)
green = PWMLED(22)

red.value = 1.0
yellow.value = 0.5
green.value = 0.1

sleep(3)
