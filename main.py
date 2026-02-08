import time
from machine import Pin
time.sleep(0.1) # Wait for USB to become ready

print("Hello, Pi Pico W!")

led_ext=Pin(15, Pin.OUT)

led = Pin('LED',Pin.OUT)

while True:
    led.toggle()
    time.sleep(1)
    led_ext.toggle()


