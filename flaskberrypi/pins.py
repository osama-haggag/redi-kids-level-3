from gpiozero import LED
import time

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

def displayLife(leds, lifeLeft):
  for led_index in range(len(leds)):
    leds[led_index].off()
  for led_index in range(lifeLeft):
    leds[led_index].on()

displayLife(leds, 9)
time.sleep(5)

displayLife(leds, 5)
time.sleep(5)

displayLife(leds, 3)
time.sleep(5)