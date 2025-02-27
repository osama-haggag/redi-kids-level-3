import gpiozero 
from gpiozero import LED
from gpiozero.pins.mock import MockFactory
import time

# allow to run on non-pinned device (for dev)
# gpiozero.Device.pin_factory = MockFactory()

leds = {
  0: LED(5),
  1: LED(6),
  2: LED(13),
  3: LED(19),
  4: LED(26),
  5: LED(12),
  6: LED(16),
  7: LED(20),
  8: LED(21),
}

def displayLife(lifeLeft):
  for led_index in range(len(leds)):
    leds[led_index].off()
  for led_index in range(lifeLeft):
    leds[led_index].on()
    
def win():
  for i in range(8):
    for led_index in range(len(leds)):
      leds[led_index].on()
      time.sleep(0.05)
      leds[led_index].off()