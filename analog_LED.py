from gpiozero import PWMLED
from time import sleep

led1 = PWMLED(18)
led2 = PWMLED(12)
led3 = PWMLED(13)

while True:

    # Increase brightness
    for brightness in range(0, 101):
        level = brightness / 100

        led1.value = level
        led2.value = level
        led3.value = level

        sleep(0.01)

    # Decrease brightness
    for brightness in range(100, -1, -1):
        level = brightness / 100

        led1.value = level
        led2.value = level
        led3.value = level

        sleep(0.01)



#------------------------------------



# from gpiozero import PWMLED
# from time import sleep

# led1 = PWMLED(18)
# led2 = PWMLED(12)
# led3 = PWMLED(13)

# while True:

#     led1.value = 0.2
#     led2.value = 0.5
#     led3.value = 1.0

#     sleep(2)

#     led1.value = 1.0
#     led2.value = 0.5
#     led3.value = 0.2

#     sleep(2)
