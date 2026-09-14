from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

led1.on()
led2.off()
led3.off()
sleep(1)

led1.off()
led2.on()
led3.off()
sleep(1)

led1.off()
led2.off()
led3.on()
sleep(1)