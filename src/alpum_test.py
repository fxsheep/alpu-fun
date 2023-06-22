from machine import Pin, I2C
from alpum import ALPUM
import time

sda = Pin(12)
scl = Pin(13)

i2c = I2C(sda=sda, scl=scl)

alpum = ALPUM(i2c)

print(alpum.bypass([0xaa, 0xa9, 0xa8, 0xa7, 0xa6, 0xa5, 0xa4, 0xa3]))

