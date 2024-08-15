import tm1637
from machine import Pin,SoftI2C
import ssd1306
import time


i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

tm = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
tm.brightness(5)

mvdetect = Pin(9, Pin.IN, Pin.PULL_UP)
rled = Pin(14,Pin.OUT)
buzz = Pin(28, Pin.OUT)
numdetect = 0
while True:
  oled.fill(0)
  oled.text('Nombre de detect', 0, 0)
  a = str(numdetect)
  oled.text(f' {a} fois',0,10)

  oled.show()
  if mvdetect.value() == 0:
    print("No detect")
    rled.off()
    tm.scroll('NOTHING',delay=250)
    time.sleep(3)
  else:
    rled.on()
    tm.show("OOOO",colon=False)
    time.sleep(0.4)
    tm.show("ccc",colon=False)
    time.sleep(0.4)
    tm.show("OOOO",colon=False)
    buzz.high()
    numdetect += 1
    print("detect")
    oled.fill(0)
    oled.text('ATTENTION', 0, 0)
    oled.text('Detection', 0, 10)
    oled.show()
    time.sleep(1)
    buzz.low()
  

    


    

  time.sleep(1)

