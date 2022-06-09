import machine
import utime

sleep_time = 0.5

def transition(red,yellow,green):
    if red.value() == 1:
        yellow.value(1)
        utime.sleep(sleep_time)
        green.value(1)
        utime.sleep(sleep_time)
    elif yellow.value() == 1:
        red.value(1)
        utime.sleep(sleep_time)
        green.value(1)
        utime.sleep(sleep_time)
    elif green.value() == 1:
        yellow.value(1)
        utime.sleep(sleep_time)
        red.value(1)
        utime.sleep(sleep_time)
    return
    

green_led = machine.Pin(15,machine.Pin.OUT)
green_button = machine.Pin(10,machine.Pin.IN,machine.Pin.PULL_DOWN)

yellow_led = machine.Pin(14,machine.Pin.OUT)
yellow_button = machine.Pin(11,machine.Pin.IN,machine.Pin.PULL_DOWN)

red_led = machine.Pin(13,machine.Pin.OUT)
red_button = machine.Pin(12,machine.Pin.IN,machine.Pin.PULL_DOWN)

while True:
  if green_button.value() == 1:
      print("green button")
      if green_led.value()==1:
          green_led.value(0)
      else:
          green_led.value(1)
      transition(red_led,yellow_led,green_led)
      red_led.value(0)
      yellow_led.value(0)
      utime.sleep(0.5)
  if yellow_button.value() == 1:
      print("yellow button")

      if yellow_led.value()==1:
          yellow_led.value(0)
      else:
          yellow_led.value(1)
      transition(red_led,yellow_led,green_led)
      green_led.value(0)
      red_led.value(0)
      utime.sleep(0.5)
  if red_button.value() == 1:
      print("red button")
      if red_led.value()==1:
          red_led.value(0)
      else:
          red_led.value(1)
      transition(red_led,yellow_led,green_led)
      yellow_led.value(0)
      green_led.value(0)
      utime.sleep(0.5)