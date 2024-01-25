from machine import *
from pico_i2c_lcd import I2cLcd
import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(13), 8)

i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# np[0] = [255, 255, 255]
# np.write()
for i in range(0, 8):
    np[i] = [255, 0, 0]
    np.write()
    time.sleep(0.1)
for i in range(0, 8):
    np[i] = [0, 0, 0]
    np.write()
    time.sleep(0.2)


def lcd_display(data, line):
    # lcd.clear()
    if len(data) <= 16:
        lcd.move_to(0, line)
        lcd.putstr(data)
        time.sleep(0.4)
    else:
        for i in range(len(data) - 15):
            lcd.move_to(0, line)
            lcd.putstr(data[i:i + 16])
            time.sleep(0.4)
        lcd.move_to(0, line)
        if len(data) > 16:
            splitat = 16
            data = data[:splitat]
        lcd.putstr(data)


while True:
    data = input()
    datalist = data.split('Hallo_docent_dit_is_onze_seperator_<3', 3)
    data = datalist[0]
    naam = datalist[1]
    print(datalist)
    if datalist[2] != "game_playing":
        gameplaying = datalist[2]
        # time.sleep(2)
        lcd.clear()
        lcd_display(naam,0)
    else:
        gameplaying = "gameplaying"
    # lcd.move_to(0, 0)
    # lcd.putstr(naam)

    # lcd_display(naam,0)
    # print(f"data = {data}")
    if data == "1":
        # if gameplaying != "gameplaying":
            # lcd.move_to(0, 1)
            # lcd.putstr(gameplaying)
        np[0] = [0, 0, 100]
        np.write()
        np[1] = [0, 0, 100]
        np.write()
        np[2] = [0, 255, 0]
        np.write()
        np[3] = [0, 255, 0]
        np.write()
        np[4] = [0, 255, 0]
        np.write()
        np[5] = [0, 255, 0]
        np.write()
        np[6] = [0, 0, 100]
        np.write()
        np[7] = [0, 0, 100]
        np.write()
        if gameplaying != "gameplaying":
            lcd_display(gameplaying, 1)
        else:
            lcd.move_to(0, 1)
            lcd.putstr(f'Online          ')


    elif data == "0":
        lcd.move_to(0, 1)
        lcd.putstr(f'Offline         ')
        np[0] = [0, 0, 200]
        np.write()
        np[1] = [0, 0, 200]
        np.write()
        np[2] = [255, 0, 0]
        np.write()
        np[3] = [255, 0, 0]
        np.write()
        np[4] = [255, 0, 0]
        np.write()
        np[5] = [255, 0, 0]
        np.write()
        np[6] = [0, 0, 200]
        np.write()
        np[7] = [0, 0, 200]
        np.write()
    elif data == "2":
        lcd.move_to(0, 1)
        lcd.putstr(f'Away            ')
        print("away")
        np[0] = [0, 0, 200]
        np.write()
        np[1] = [0, 0, 200]
        np.write()
        np[2] = [255, 50, 0]
        np.write()
        np[3] = [255, 50, 0]
        np.write()
        np[4] = [255, 50, 0]
        np.write()
        np[5] = [255, 50, 0]
        np.write()
        np[6] = [0, 0, 200]
        np.write()
        np[7] = [0, 0, 200]
        np.write()
    elif data == "3":
        lcd.move_to(0, 1)
        lcd.putstr(f'Snooze     ')
        np[0] = [0, 0, 200]
        np.write()
        np[1] = [0, 0, 200]
        np.write()
        np[2] = [255, 200, 0]
        np.write()
        np[3] = [255, 200, 0]
        np.write()
        np[4] = [255, 200, 0]
        np.write()
        np[5] = [255, 200, 0]
        np.write()
        np[6] = [0, 0, 200]
        np.write()
        np[7] = [0, 0, 200]
        np.write()
    else:
        np[0] = [255, 0, 0]
        np.write()





#
#     np[0] = [0, 0, 200]
#     np.write()
#
#     np[1] = [0, 0, 200]
#     np.write()
#
#     np[2] = [0, 255, 0]
#     # time.sleep(1)
#     np.write()
#
#     np[3] = [255, 0, 0]
#     # time.sleep(1)
#     np.write()
#
#
#     np[4] = [255, 50, 0]
#     # time.sleep(1)
#     np.write()
#
#     np[5] = [255, 200, 0]
#     # time.sleep(1)
#     np.write()
#
#     np[6] = [0, 0, 200]
#     np.write()
#
#     np[7] = [0, 0, 200]
#     np.write()
# import time
#
# import machine
# import neopixel






